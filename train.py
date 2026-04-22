import os
import cv2
import torch
from torch.utils.data import Dataset,DataLoader
from torchvision import transforms
import torch.nn as nn
from model import BrainTumorGravityModel

class BrainDataset(Dataset):

    def __init__(self,root,transform=None):

        self.images=[]
        self.labels=[]
        self.transform=transform

        classes={"normal":0,"lgg":1,"hgg":2}

        for folder in classes:

            path=os.path.join(root,folder)

            for img in os.listdir(path):

                self.images.append(os.path.join(path,img))
                self.labels.append(classes[folder])

    def __len__(self):
        return len(self.images)

    def __getitem__(self,idx):

        img=cv2.imread(self.images[idx])
        img=cv2.resize(img,(224,224))

        if self.transform:
            img=self.transform(img)

        label=torch.tensor(self.labels[idx])

        return img,label


transform=transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((128,128)),
    transforms.ToTensor()
])

dataset=BrainDataset("dataset",transform)

loader=DataLoader(dataset,batch_size=16,shuffle=True, num_workers=2)

device=torch.device("cuda" if torch.cuda.is_available() else "cpu")

model=BrainTumorGravityModel().to(device)

criterion=nn.CrossEntropyLoss()

optimizer=torch.optim.Adam(model.parameters(),lr=0.0001)

for epoch in range(10):

    for imgs,labels in loader:

        imgs=imgs.to(device)
        labels=labels.to(device)

        outputs=model(imgs)

        loss=criterion(outputs,labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print("Epoch:",epoch,"Loss:",loss.item())

torch.save(model.state_dict(),"brain_model.pth")
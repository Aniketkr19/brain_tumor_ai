import streamlit as st
import torch
import cv2
import numpy as np
from PIL import Image
from torchvision import transforms
from model import BrainTumorGravityModel

st.title("Brain Tumor Gravity Detection System")

st.write("Upload MRI image to detect tumor severity")

device=torch.device("cpu")

model=BrainTumorGravityModel()

model.load_state_dict(torch.load("brain_model.pth",map_location=device))

model.eval()

transform=transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])

classes=["Normal Brain",
         "Low Grade Tumor (Moderate)",
         "High Grade Tumor (Severe)"]

uploaded_file=st.file_uploader("Upload MRI Image",type=["jpg","png"])

if uploaded_file is not None:

    image=Image.open(uploaded_file).convert("RGB")

    st.image(image,caption="Uploaded MRI",use_column_width=True)

    img=transform(image).unsqueeze(0)

    with torch.no_grad():

        output=model(img)

        probs=torch.softmax(output,dim=1)

        pred=torch.argmax(probs,1).item()

    st.subheader("Diagnosis Result")

    st.success(classes[pred])

    st.subheader("Model Confidence")

    st.bar_chart(probs.numpy()[0])
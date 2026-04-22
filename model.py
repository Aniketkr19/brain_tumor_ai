import torch
import torch.nn as nn
import timm

class BrainTumorGravityModel(nn.Module):

    def __init__(self):

        super().__init__()

        # CNN feature extractor
        self.backbone = timm.create_model(
            "resnet34",
            pretrained=True,
            num_classes=0
        )

        # Attention layer
        self.attention = nn.MultiheadAttention(
            embed_dim=512,
            num_heads=8,
            batch_first=True
        )

        # classifier
        self.classifier = nn.Sequential(
            nn.Linear(512,256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256,3)
        )

    def forward(self,x):

        features = self.backbone(x)

        features = features.unsqueeze(1)

        attn_output,_ = self.attention(
            features,
            features,
            features
        )

        attn_output = attn_output.squeeze(1)

        output = self.classifier(attn_output)

        return output
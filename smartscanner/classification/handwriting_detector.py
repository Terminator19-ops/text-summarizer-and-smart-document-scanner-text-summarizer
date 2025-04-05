# classification/handwriting_detector.py
import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image

# Load pretrained model (simulate 2-class classification)
model = models.mobilenet_v2(pretrained=True)
model.classifier[1] = torch.nn.Linear(model.last_channel, 2)  # handwritten or typed
model.eval()

# Simulated model – in production, use a fine-tuned version

# Transformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

labels = ['handwritten', 'typed']

def predict_handwriting(image_path):
    image = Image.open(image_path).convert("RGB")
    img_tensor = transform(image).unsqueeze(0)  # Add batch dim

    with torch.no_grad():
        outputs = model(img_tensor)
        predicted = torch.argmax(outputs, dim=1).item()

    return labels[predicted]

# doc_type_classifier/type_classifier.py
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

# Load model and tokenizer
model_name = "nbroad/roberta-base-docclassification"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

labels = [
    'Resume', 'Invoice', 'Research Paper', 
    'Letter', 'Certificate', 'Bill'
]

UNKNOWN_THRESHOLD = 0.5  # You can tweak this for sensitivity

def classify_document(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    with torch.no_grad():
        outputs = model(**inputs)
        probs = F.softmax(outputs.logits, dim=1)
        confidence, predicted_class = torch.max(probs, dim=1)

    if confidence.item() < UNKNOWN_THRESHOLD:
        return "Unknown"
    
    return labels[predicted_class.item()]

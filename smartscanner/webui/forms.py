# webui/forms.py
from django import forms

class UploadForm(forms.Form):
    document = forms.ImageField(label='Upload a scanned document')
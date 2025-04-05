from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.base import ContentFile
import base64
import re

def upload_document_view(request):
    """
    View function to render the document upload template.
    """
    return render(request, 'upload_document.html')

def process_document(request):
    """
    View function to process the uploaded document or camera capture.
    """
    if request.method == 'POST':
        document = None
        
        # Handle file upload
        if 'document' in request.FILES:
            document = request.FILES['document']
            
        # Handle camera data (if no file was uploaded but we have camera data)
        elif 'camera_data' in request.POST and request.POST['camera_data']:
            # Extract the base64 encoded image data
            image_data = request.POST['camera_data']
            
            # Check if it's a data URL and extract the base64 part
            if image_data.startswith('data:'):
                # Extract the content type and base64 data
                format, imgstr = re.match(r'data:image/(?P<format>.*?);base64,(?P<imgstr>.*)', image_data).groups()
                
                # Decode the base64 data and create a ContentFile
                data = base64.b64decode(imgstr)
                document = ContentFile(data, name=f'camera_capture.{format}')
        
        if document:
            # Process the document - here you would typically save to a model
            # Example with a Document model:
            # from .models import Document
            # doc = Document(name=document.name, file=document)
            # doc.save()
            
            # Add a success message
            messages.success(request, f'Document "{document.name}" uploaded successfully!')
            
            # Redirect to a success page or back to the upload page
            return render(request, 'upload_document.html', {'success': True})
        else:
            messages.error(request, 'No document was uploaded or captured.')
    
    # If not POST or no file uploaded, redirect back to the upload page
    return redirect('upload_document')
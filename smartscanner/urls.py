from django.urls import path
from . import views

app_name = 'document_app'  # This creates a namespace for your app URLs

urlpatterns = [
    path('upload/', views.upload_document_view, name='upload_document'),
    path('process/', views.process_document, name='process_document'),
]
from django import forms
from .models import File

class fileeuploadform(forms.ModelForm):
    class Meta:
        model = File
        fields = ['files']
from django.forms import ModelForm
from .models import Image, Tag

# Create the form class.
class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        

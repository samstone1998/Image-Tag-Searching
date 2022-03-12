from google.cloud import vision
from celery import shared_task
import io
import os

from .models import Image, Tag

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="../django-image-search-f9ff8c0300dc.json"



@shared_task
def get_tags(image_name, image_pk):
    client = vision.ImageAnnotatorClient()
    imageobj = Image.objects.get(pk=image_pk)
    tags = []
    
    with io.open(image_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    
    response = client.label_detection(image=image)
    labels = [tags.append(label.description) for label in response.label_annotations]
    
    text = client.text_detection(image=image)
    texts = text.text_annotations
    text = [i.description.strip() for i in texts]
    text = ' '.join(text)
    if text:
        tags.append(text)

    for tag in tags:
        try:
            Tag.objects.create(image=imageobj, tag=tag)
        except:
            pass

    return

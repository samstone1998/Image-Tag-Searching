from django.db import models

import uuid

class Image(models.Model):
    def generate_name(instance, filename):
        extension = filename.split('.')[-1]
        return f'{uuid.uuid4().hex}.{extension}'
        
    image = models.ImageField(upload_to=generate_name)
    upload_time = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    image = models.ForeignKey(to=Image, on_delete=models.CASCADE)
    tag = models.CharField(max_length=200, blank=False, null=False)
    
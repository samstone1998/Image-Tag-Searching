from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect


from .forms import ImageForm
from .models import Image, Tag

from celery import shared_task

from .tasks import get_tags


class home(View):
    def get(self, request):
        query = request.GET.get('q')
        if query:
            images = Tag.objects.filter(tag__search=query).select_related('image').only('image').distinct('image')
        else:
            images = Image.objects.all()

        form = ImageForm()
        return render(request, 'frontend/home.html', {
            'form': form,
            'images': images
        })
    
    def post(self, request):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            get_tags.delay(image_name=str(obj.image.path), image_pk=obj.pk)     
            return redirect('home')
        
        images = Image.objects.all()
        
        return render(request, 'frontend/home.html', {
            'form': form,
            'images': images
        })
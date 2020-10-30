from django.shortcuts import render, get_object_or_404
from .models import Life
# Create your views here.


def all_photos(request):
    photos = Life.objects.order_by('-date')
    return render(request, 'life/all_photos.html', {'photos': photos})

def detail(request, photo_id):
    photo = get_object_or_404(Life, pk=photo_id)
    return render(request, 'life/detail.html',{'photo':photo})
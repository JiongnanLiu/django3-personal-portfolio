from django.shortcuts import render, get_object_or_404
from .models import myBlog
# Create your views here.


def all_blogs(request):
    blogs = myBlog.objects.order_by('date')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(myBlog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})

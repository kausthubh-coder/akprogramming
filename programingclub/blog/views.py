from django.shortcuts import render
from django.db.models import Q
from .models import Blog
# Create your views here.
def index(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    blogs = Blog.objects.filter(
        Q(title__icontains=q) |
        Q(description__icontains=q) 
    ) 

    blogs_count = blogs.count()

    return render(request,"blog/index.html",{"blogs":blogs})

def single_blog(request,id):
    print(id)
    blog = Blog.objects.get(pk=id)
    return render(request,"blog/blog.html",{"blog":blog})

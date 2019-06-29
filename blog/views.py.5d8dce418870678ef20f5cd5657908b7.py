from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from .form import BlogPost
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponseNotFound
# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request,'home.html',{'blogs':blogs, 'user':request.user})

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'blog':blog_detail, 'user':request.user, 'blog_id': str(blog_id)})

def create(request):
    blog=Blog()
    blog.title=request.POST['title']
    blog.body= request.POST['body']
    blog.pub_date=timezone.datetime.now()
    blog.author = request.user
    blog.save()
    return redirect('/blog/'+str(blog.id))

def edit(request,blog_id):
    blog = get_object_or_404(Blog,pk = blog_id)
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.save()
        return redirect('/blog/' + str(blog.id))
    else:
        return render(request,'edit.html',{'blog':blog})
        
def delete(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    blog.delete()
    return redirect('/')
    


def blogpost(request):
    #1. 입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST' :
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.author = request.user
            post.save()
            return redirect('home')

    #2.빈페이지를 띄워주는 기능 ->GET
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})

def search(request):
    if request.method == 'POST':
        blogList = Blog.objects.filter(title__icontains=request.POST['search'])
        return render(request, 'search.html', {'blogs': blogList, 'user': request.user})
    else:
        return HttpResponseNotFound("없는 페이지 입니다.")
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost

def blog_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog_list.html', {'blog_posts': blog_posts})

def blog_detail(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_detail.html', {'blog_post': blog_post})

# Add CRUD functionality: create, update, delete

def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user

        blog_post = BlogPost(title=title, content=content, author=author)
        blog_post.save()
        return redirect('blog_list')
    return render(request, 'create_blog.html')

def update_blog(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        blog_post.title = title
        blog_post.content = content
        blog_post.save()
        return redirect('blog_list')
    return render(request, 'update_blog.html', {'blog_post': blog_post})

def delete_blog(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    blog_post.delete()
    return redirect('blog_list')


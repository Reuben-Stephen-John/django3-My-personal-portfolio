from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def blog(request):
    blog_count=Blog.objects.count()
    blog_5=Blog.objects.order_by()[:5]
    Blogs=Blog.objects.all()
    return render(request,'blog/blogs.html',{'blogs':Blogs})
def detail (request, blog_id):
    blog= get_object_or_404(Blog, pk=blog_id)
    return render (request, 'blog/detail.html',{'blog':blog})

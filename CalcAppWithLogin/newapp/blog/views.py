from django.shortcuts import render
from .models import BlogDetails
from datetime import date

# Create your views here.
def blog(request):
        if request.method == 'POST':
                blog_title = request.POST.get('blog_title')
                blog_author = request.user
                blog_details = request.POST.get('blog_details')
                c = BlogDetails(blog_title=blog_title,blog_author=blog_author,blog_details=blog_details, date='2020-12-12', time ='18:20')

                c.save()
                blog = BlogDetails.objects.all
                return render(request, 'blog/blog.html', {'blog': blog})
        else:
                blog = BlogDetails.objects.all
                return render(request, 'blog/blog.html', {'blog' : blog})

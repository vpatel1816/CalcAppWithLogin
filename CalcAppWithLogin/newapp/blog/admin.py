from django.contrib import admin
from .models import BlogDetails
# Register your models here.

class Blog(admin.ModelAdmin):
    list_display = ('blog_title','blog_author')


admin.site.register(BlogDetails, Blog)
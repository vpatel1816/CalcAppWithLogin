from django.db import models
from datetime import date

# Create your models here.
class BlogDetails(models.Model):
    blog_title = models.CharField(max_length=30)
    blog_details = models.TextField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    blog_author = models.CharField(max_length=20)

    def __str__(self):
        return self.blog_title
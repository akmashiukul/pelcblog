from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django.db.models.base import Model
from django.db.models.signals import pre_save
from blog.utils import unique_slug_generator
from django.utils.timezone import now

# Create your models here.
class PostComment(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.get_username()}'
class Question(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField(default="")
    class_name=models.CharField(default="",max_length=3)

    def __str__(self):
        return f'{self.sender.get_username()}'

class Categories(models.Model):
    categoryname = models.CharField(max_length=255)

    def __str__(self):
        return self.categoryname

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='Blog Post')
    slug = models.SlugField(max_length=255, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=1555,default=None)
    comments = models.ManyToManyField(PostComment, blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categories, null=True, on_delete=models.PROTECT, related_name='category_set')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Post)
class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)
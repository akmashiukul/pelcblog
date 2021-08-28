from django.contrib import admin
from .models import Post, Categories, PostComment,Question,BlogComment

# Register your models here.
admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(Categories)
admin.site.register(Question)
admin.site.register(BlogComment)

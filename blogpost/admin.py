from django.contrib import admin

from blogpost.models import Author, Blogs, Comments, Likes, Post

# Register your models here.

admin.site.register(Blogs)
admin.site.register(Comments)
admin.site.register(Likes)

admin.site.register(Author)
admin.site.register(Post)

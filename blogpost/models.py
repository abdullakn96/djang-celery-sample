from statistics import mode
from django.db import models

# Create your models here.



class Blogs(models.Model):
    blog_title=models.CharField(max_length=200)
    blog_description  = models.TextField()
    blog_date = models.DateField(auto_created=True)


class Comments(models.Model):
    comments=models.CharField(max_length=200)
    blog=models.ForeignKey(Blogs,on_delete=models.CASCADE,related_name='realated_comment')


class Likes(models.Model):
    likes=models.IntegerField()
    blog=models.ForeignKey(Blogs,on_delete=models.CASCADE,related_name='related_likes')    





class Author(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField(blank=True)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.title        



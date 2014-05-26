from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=20)
    content=models.TextField()
    time=models.DateTimeField(null=True)
    username=models.ForeignKey(User)


class News(models.Model):
    title=models.CharField(max_length=20)
    content=models.TextField()
    time=models.DateTimeField()
   # downfile=models.FileField(upload_to='album/%m-%Y/')

    
class regUser(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class Message(models.Model):
    email=models.CharField(max_length=20)
    content=models.TextField()

class dangerWord(models.Model):
    word=models.CharField(max_length=30)


class Comment(models.Model):
    username=models.ForeignKey(User)
    content=models.TextField()
    time=models.DateTimeField()
    blog=models.ForeignKey(Blog)


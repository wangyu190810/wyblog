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
    
class regUser(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class Message(models.Model):
    email=models.CharField(max_length=20)
    content=models.TextField()



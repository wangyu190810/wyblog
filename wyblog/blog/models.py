from django.db import models
from django.contrib.auth.models import User
from markupfield.fields import MarkupField
from tinymce.models import HTMLField
#from markitup.fields import MarkupField
# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=20)
    content=models.TextField()
    time=models.DateTimeField(null=True)
    username=models.ForeignKey(User)
    def __unicode__(self):
        return u"%s %s"%(self.title,self.time)


class News(models.Model):
    title=models.CharField(max_length=20)
    content=models.TextField()
    time=models.DateTimeField()
    downfile=models.FileField("File",upload_to='news',max_length=100)
    def __unicode__(self):
        return u"%s %s"%(self.title,self.time)

    
class regUser(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    lab=models.IntegerField(null=True)

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
#
class Honor(models.Model):
    title=models.CharField(max_length=20)
    body=MarkupField()
    downfile=models.FileField("Honor",upload_to="honor",max_length=100)
    
class MyModel(models.Model):
    content=HTMLField()


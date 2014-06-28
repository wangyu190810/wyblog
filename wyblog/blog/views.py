#-*-coding:utf-8-*-
from django.shortcuts import render_to_response,HttpResponse
from django.http import HttpResponseRedirect
from models import regUser,Message,Blog,Comment,News,Honor
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.template import RequestContext
from django.core.paginator import Paginator

import time
#import tt
def index(request):
    
    return render_to_response('index.html',{"username":request.user})

def loginuser(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            id=request.user.id
            blog=Blog.objects.filter(username_id=id)
            return render_to_response('user.html',{"username":user,'blog':blog},context_instance=RequestContext(request))
        else:
            error=True
            return render_to_response('login.html',{"error":error},context_instance=RequestContext(request))
    return render_to_response('login.html',
            context_instance=RequestContext(request))

def register(request):
    if request.method=="POST":
        if request.POST['password']==request.POST['rpassword']:
            testuser=User.objects.filter(username=request.POST['username'])
            if not len(testuser):

                user=User.objects.create_user(
                        email= request.POST['email'],
                    username=request.POST['username'],
                    password= request.POST['password']
                    )
                user.save()
                return HttpResponseRedirect('/login')
            test=True
            return render_to_response('register.html',{"test":True},context_instance=RequestContext(request))
        error=True
        return render_to_response('register.html',{"error":error},context_instance=RequestContext(request))
        
    return render_to_response('register.html',
            context_instance=RequestContext(request))

# Create your views here.
def message(request):
    error=False
    if request.method=="POST":
        if request.POST['Email']:
            M=Message(email=request.POST['Email'],
                content=request.POST['content'])
            M.save()
            return HttpResponseRedirect('/contact')
        error=True

    userMessage=Message.objects.all()
    return render_to_response('contact.html',{"message":userMessage,"error":error},context_instance=RequestContext(request))

def blog(request):
    if not request.user.is_authenticated():
        return render_to_response('login.html',context_instance=RequestContext(request))
    if request.method=="POST":

        a=request.user.id
        blog=Blog(title=request.POST['title'],
                content=request.POST['content'],
                time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),
                username_id=request.user.id)
        blog.save()
        return render_to_response('user.html',context_instance=RequestContext(request))

    return render_to_response('blog.html',context_instance=RequestContext(request))
def listBlog(request):
    pagenum=1
    if request.REQUEST.has_key("pid"):
        pagenum=request.REQUEST['pid']
    blogall=Blog.objects.order_by("-id")
    p=Paginator(blogall,3)
    page=p.page(pagenum)

    return render_to_response('listblog.html',{"p":p,"page":page,"username":request.user})

def readBlog(request):
    showblog={}
    edit=False
    comment=Comment
    if request.GET.has_key('pid'):
        
        username_id=request.user.id
        rblog=Blog.objects.get(id=request.GET['pid'])
        usernameID= rblog.username_id
        user=User.objects.get(id=usernameID)
        if rblog:
            showblog['title']=rblog.title
            showblog['id']=rblog.id
            showblog['content']=rblog.content
            showblog['time']=rblog.time
            showblog['username']=user.username
            if request.method=="POST":
                if not request.user.is_authenticated():
                    return HttpResponseRedirect('login')
                content=request.POST['content']
                blog_id=rblog.id
                comment=Comment(username_id=username_id,
                        content=content,
                        time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),
                        blog_id=blog_id)
                comment.save()
            if request.method=="GET":
                if username_id==usernameID:
                    edit=True
        
            comment=Comment.objects.filter(blog_id=request.GET['pid'])
    return render_to_response('readblog.html',{"blog":showblog,"comment":comment,"edit":edit},context_instance=RequestContext(request))

def user(request):
    blog=None
    if request.GET.has_key("pid"):
        user=User.objects.get(username=request.GET['pid']) 
        requsername=request.user.username
        blog=Blog.objects.filter(username_id=user.id)
        bloglist=blog.order_by('-id')
    
    return render_to_response('user.html',{"username":request.GET['pid'],"requser":requsername,"blog":bloglist})

def about_me(request):
    return render_to_response('about.html')

def artwork(request):
    return render_to_response('artwork.html')

def people(request):
    user=User.objects.all()
    return render_to_response('member.html',{"user":user})
def updateblog(request):
    blog=None
    if request.GET.has_key("pid"):
        blog=Blog.objects.get(id=request.GET['pid'])
        if request.method=="POST":
            blog.title=request.POST['title'] 
            blog.content=request.POST['content']
            blog.save()
            return HttpResponseRedirect('/index')
    return render_to_response('updateblog.html',{"blog":blog},context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return render_to_response('index.html')

def honor(request):
    hon=Honor.objects.all()
    return render_to_response('honor.html',{"honor":hon})
def news(request):
    news=News.objects.order_by("-id")
    return render_to_response("newslist.html",{"news":news})
def readnews(request):
    new=None
    if request.GET.has_key("pid"):
        new=News.objects.get(id=request.GET['pid'])
    return render_to_response("new.html",{"new":new})


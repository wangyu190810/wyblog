from django.shortcuts import render_to_response,HttpResponse
from models import regUser,Message,Blog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
import time

def index(request):
    
    return render_to_response('index.html')

def loginuser(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            id=request.user.id
            blog=Blog.objects.filter(username_id=id)
            return render_to_response('user.html',{"username":user,'blog':blog})
    return render_to_response('login.html',)

def register(request):
    if request.method=="POST":
        user=User.objects.create_user(
                email= request.POST['email'],
            username=request.POST['username'],
            password= request.POST['password']
                )
        user.save()
    return render_to_response('register.html')

# Create your views here.
def message(request):
    if request.method=="POST":
        if request.POST['email']:
            M=Message(email=request.POST['email'],
                content=request.POST['content'])
            M.save()
    error="You must input your email"

    userMessage=Message.objects.all()
    return render_to_response('Message.html',{"Messages":userMessage,"error":error})

def blog(request):
    if not request.user.is_authenticated():
        return render_to_response('login.html')
    if request.method=="POST":
        if request.POST['title']:
            blog=Blog(title=request.POST['title'],
                    content=request.POST['content'],
                    time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),
                    username_id=request.user.id)
            blog.save()
        return render_to_response('user.html')

    return render_to_response('blog.html')
def listBlog(request):
    bloglist=Blog.objects.order_by('-id')
    return render_to_response('listblog.html',{"blog":bloglist})

def readBlog(request,r_id):
    showblog={}
    rblog=Blog.objects.get(id=r_id)
    usernameID= rblog.username_id
    user=Blog.objects.get(id=usernameID)

    if rblog:
        showblog['title']=rblog.title
        showblog['content']=rblog.content
        showblog['time']=rblog.time
        showblog['username']=user.username
    return render_to_response('readblog.html',{"blog":showblog})

def user(request):
    blog=None
    if request.GET.has_key("pid"):
        user=User.objects.get(username=request.GET['pid']) 
        blog=Blog.objects.filter(username_id=user.id)
    return render_to_response('user.html',{"username":request.GET['pid'],"blog":blog})



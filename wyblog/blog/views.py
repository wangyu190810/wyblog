#-*-coding:utf-8-*-
from django.shortcuts import render_to_response,HttpResponse
from django.http import HttpResponseRedirect
from models import regUser,Message,Blog,Comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import time
#import tt
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
        else:
            error=True
            return render_to_response('login.html',{"error":error})
    return render_to_response('login.html',)

def register(request):
    if request.method=="POST":
        if request.POST['password']==request.POST['rpassword']:
            testuser=User.objects.filter(username=request.POST['username'])
            print len(testuser)
            pa=[]
            if not len(testuser):

                user=User.objects.create_user(
                        email= request.POST['email'],
                    username=request.POST['username'],
                    password= request.POST['password']
                    )
                user.save()
                return HttpResponseRedirect('/login')
            test=True
            return render_to_response('register.html',{"test":True})
        error=True
        return render_to_response('register.html',{"error":error})
        
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
    return render_to_response('contact.html',{"Messages":userMessage,"error":error})

def blog(request):
    if not request.user.is_authenticated():
        return render_to_response('login.html')
    if request.method=="POST":

        a=request.user.id
        print dir(a)
        print "asdfasdfasdf"
        blog=Blog(title=request.POST['title'],
                content=request.POST['content'],
                time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),
                username_id=request.user.id)
        blog.save()
        return render_to_response('user.html')
    print request.user.id

    return render_to_response('blog.html')
def listBlog(request):
    bloglist=Blog.objects.order_by('-id')
    return render_to_response('listblog.html',{"blog":bloglist})

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
    
        if username_id==usernameID:
            edit=True
        
        comment=Comment.objects.filter(blog_id=request.GET['pid'])
    return render_to_response('readblog.html',{"blog":showblog,"comment":comment,"edit":edit})

def user(request):
    blog=None
    if request.GET.has_key("pid"):
        user=User.objects.get(username=request.GET['pid']) 
        requsername=request.user.username
        blog=Blog.objects.filter(username_id=user.id)
    
    return render_to_response('user.html',{"username":request.GET['pid'],"requser":requsername,"blog":blog})

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
        print dir(Blog.comment_set)
        if request.method=="POST":
            blog.title=request.POST['title'] 
            blog.content=request.POST['content']
            blog.save()
            return render_to_response('index.html')

    return render_to_response('updateblog.html',{"blog":blog})


def logout_view(request):
    logout(request)
    return render_to_response('index.html')

def honor(request):
    return render_to_response('honor.html')

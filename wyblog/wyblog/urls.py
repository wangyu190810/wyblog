from django.conf.urls import patterns, include, url
from blog.views import index,register,message,\
        blog,listBlog,readBlog,loginuser,user,\
        people,artwork,about_me,updateblog,logout_view,\
        honor,news,readnews
        
# Uncomment the next two lines to enable the admin:
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wyblog.views.home', name='home'),
    # url(r'^wyblog/', include('wyblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$',index),
    url(r'^index',index),
    url(r'^login',loginuser),
    url(r'^register',register),
    url(r'^contact',message),
    url(r'^blog',blog),
    url(r'^listblog',listBlog),
    url(r'^user',user),
    url(r'^readblog',readBlog),
    url(r'^member',people),
    url(r'^artwork',artwork),
    url(r'^about',about_me),
    url(r'^updateblog',updateblog),
#    url(r'^\d+/$',testtime),
    url(r'^logout',logout_view),
    url(r'^honor',honor),
    url(r'^new',news),
    url(r"^readnews",readnews),
    # Uncomment the next line to enable the admin:
    url(r"^markdown/",include('django_markdown.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'media/(?P<path>.*)$',"django.views.static.serve",{"document_root":'./media'}),
)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



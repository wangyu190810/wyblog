from django.conf.urls import patterns, include, url
from blog.views import index,register,message,\
        blog,listBlog,readBlog,loginuser,user,\
        people,artwork,about_me,updateblog
        
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
    url(r'^login',loginuser),
    url(r'^register',register),
    url(r'^message',message),
    url(r'^blog',blog),
    url(r'^listblog',listBlog),
    url(r'^user',user),
    url(r'^readblog/(\d{1,5})$',readBlog),
    url(r'^people',people),
    url(r'^artwork',artwork),
    url(r'^about_me',about_me),
    url(r'^updateblog',updateblog),
#    url(r'^\d+/$',testtime),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



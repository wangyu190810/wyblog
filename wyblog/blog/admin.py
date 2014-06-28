from models import Blog,News,Message,dangerWord,regUser,Honor,MyModel
from django.contrib import admin

class NewsAdmin(admin.ModelAdmin):
    list_dispaly=('title','time')

class BlogAdmin(admin.ModelAdmin):
    list_dispaly=('title','time')

admin.site.register(Blog)
admin.site.register(News,NewsAdmin)
admin.site.register(Message)
admin.site.register(dangerWord)
admin.site.register(regUser)
admin.site.register(Honor)
admin.site.register(MyModel)





from django.contrib import admin
from .models import Main,fooAbout,about_main
# Register your models here.
from django.contrib.auth.models import Group,User

admin.site.unregister(Group)
# admin.site.unregister(User)
# admin.site.register(UserManager)
admin.site.register(Main)
admin.site.register(fooAbout)
admin.site.register(about_main)
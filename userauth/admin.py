from django.contrib import admin
from userauth.models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['email','username']
admin.site.register(User,UserAdmin)
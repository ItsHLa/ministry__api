from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from accounts.models import User



# Register your models here.
class Admin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ()
    search_fields = ('username', 'email')
    readonly_fields = ('id' , 'last_login', 'date_joined')
    fieldsets = ()
    filter_horizontal = ()

def create_get_group(name):
    return Group.objects.get_or_create(name='employee')

def create_get_content_Type(model):
    return ContentType.objects.get_for_model(model)

def get_permission(codename,content_type):
    return Permission.objects.get(codename=codename, content_type=content_type)









admin.site.register(User , Admin)




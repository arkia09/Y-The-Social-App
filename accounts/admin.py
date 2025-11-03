from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User, Group
# Register your models here.

# admin.site.register(Profile)
admin.site.unregister(Group)

 #Mix Profile info with User in admins
class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
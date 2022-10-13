from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','first_name', 'last_name','email']
    list_display_links = ['id','username']
    list_filter = ['role']
    search_fields = ['email','username','first_name','last_name']

admin.site.register(User,UserAdmin)

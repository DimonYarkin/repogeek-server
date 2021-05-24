from django.contrib import admin
from authapp.models import User

# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [ 'username','id', 'first_name', 'last_name', 'email']
    ordering = ['username']
    search_fields = ['username']

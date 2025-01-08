from django.contrib import admin

# Register your models here.
from auth_system.models import CustomUser

admin.site.register(CustomUser)
from django.contrib import admin
from .models import CustomUser
from .models import Profile

admin.site.register(Profile)
admin.site.register(CustomUser)
from django.contrib import admin
from .models import Client, SignIn, Campaign

# Register your models here.
admin.site.register(Client)
admin.site.register(SignIn)
admin.site.register(Campaign)
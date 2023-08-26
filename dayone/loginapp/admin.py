from django.contrib import admin

# Register your models here.
from .models import Profile,Collection,UserCollection
admin.site.register(Profile)
admin.site.register(Collection)
admin.site.register(UserCollection)
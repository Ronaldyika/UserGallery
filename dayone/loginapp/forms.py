from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserCollection


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class GalleryForm(forms.Form):
    class Meta:
        model = UserCollection
        fields = '__all__'
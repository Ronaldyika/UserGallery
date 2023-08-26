from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework.response import Response
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'main/index.html')

def RegisterUser(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("User saved")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'users/register.html', {'form': form})
            
@login_required()
def profile(request):
    query = Profile.objects.all();
    context = {
        'query':query
    }
    return render(request,'users/profile.html',context)
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Location
from .forms import LocationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def home(request):
    locations = Location.objects.all()
    form = LocationForm()
    return render(request, 'home.html', {'locations': locations, 'form': form})

def detail(request, location_id):
    location = Location.objects.get(id=location_id)
    return render(request, 'detail.html', {'location': location})

def post_location(request):
    form = LocationForm(request.POST, request.FILES)
    if form.is_valid():
        location = form.save(commit = False)
        location.user = request.user
        location.save()
    return HttpResponseRedirect('/')
    
    
def profile(request, username):
    user = User.objects.get(username=username)
    locations = Location.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'locations': locations})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
    else:
        form = UserCreationForm()
        return render(request, 'registration.html', {'form': form})
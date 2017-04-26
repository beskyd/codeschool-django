from django.shortcuts import render
#from django.http import HttpResponse
from .models import Treasure

# Create your views here.
def index(request):
    treasures = Treasure.objects.all()
    return render(request, 'index.html' , { 'treasures': treasures })
    
    

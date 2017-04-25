from django.shortcuts import render
#from django.http import HttpResponse

def home(request):
    location_name = "Fool's Falls"
    predators = 'Scorpions, Snakes'
    context = {
        'location_name': location_name,
        'predators': predators
    }
    return render(request, 'home.html', context)

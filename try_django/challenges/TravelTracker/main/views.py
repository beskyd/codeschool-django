from django.shortcuts import render
#from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')


class Location:
    def __init__(self, name, predators, num_restaurants, img_url):
        self.name = name
        self.predators = predators
        self.num_restaurants = num_restaurants
        self.img_url = img_url
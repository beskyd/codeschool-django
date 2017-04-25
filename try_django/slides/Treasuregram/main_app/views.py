from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html' , { 'treasures': treasures })
    
    
class Treasure:
    def __init__(self, name, value, material, location, img_url):
        self.name = name
        self.value = value
        self.material = material
        self.location = location
        self.img_url = img_url
        
treasures = [
    Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM", 'example.com/nugget.jpg'),
    Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO", 'example.com/fools-gold.jpg'),
    Treasure('Coffee Can', 20.00, 'tin', 'Acme, CA', 'example.com/coffee-can.jpg')
]
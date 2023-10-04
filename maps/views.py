from django.shortcuts import render
from property.models import * 

# Create your views here.
def search_with_map(request): 
    apartments_rent = ApartmentRent.objects.all()
    context = {
        'apartments_rent': apartments_rent, 
    } 
    return render(request, 'maps/index.html', context)
from django.shortcuts import render
from .models import * 

# Create your views here.

def property_details(request, number): 
    property = ApartmentRent.objects.get(number=number) 
     
    context=  {
        'property': property, 
    } 
    return render(request, 'property/property-details.html', context ) 


def add_property(request):
    context = {} 
    return render(request, 'property/add-property-interface.html', context)



## دوال الايجار
def add_apartment_rent(request): 
    context = {} 
    return render(request, 'property/add-apartment-rent.html', context)
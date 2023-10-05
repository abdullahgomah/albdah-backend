from django.shortcuts import render
from .models import * 

# Create your views here.

def property_details(request, number): 
    property = ApartmentRent.objects.get(number=number) 
     
    context=  {
        'property': property, 
    } 
    return render(request, 'property/property-details.html', context ) 
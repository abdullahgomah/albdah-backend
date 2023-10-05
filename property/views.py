from django.shortcuts import render

# Create your views here.

def property_details(request): 
    context=  {} 
    return render(request, 'property/property-details.html', context ) 
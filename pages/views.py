from django.shortcuts import render
from .models import  * 
from property.models import * 

# Create your views here.
def home(request): 


    ## get all ads 
    apartments_rent = ApartmentRent.objects.all() 


    context = {
        'apartments_rent': apartments_rent 
    } 
    return render(request, 'pages/index.html', context)

def about(request): 
    context = {}
    return render(request, 'pages/about.html', context)


def contact(request): 
    context = {} 
    return render(request, 'pages/contact.html', context) 


def request_contract(request): 
    context= {} 
    return render(request, 'pages/request_contract.html', context)
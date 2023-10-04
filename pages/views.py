from django.shortcuts import render
from .models import  * 

# Create your views here.
def home(request): 
    context = {} 
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
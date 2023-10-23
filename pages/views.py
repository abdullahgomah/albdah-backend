from django.shortcuts import render
from .models import  * 
from property.models import * 

# Create your views here.
def home(request): 


    ## get all ads 
    apartments_rent = ApartmentRent.objects.all() 
    floors_rent = FloorRent.objects.all() 
    villas_rent = VillaRent.objects.all() 
    shops_rent = ShopRent.objects.all() 
    resthouses_rent = RestHouseRent.objects.all() 
    commercial_offices_rent = CommercialOfficeRent.objects.all() 
    lands_rent = LandRent.objects.all() 
    buildings_rent = BuildingRent.objects.all() 
    warehouses_rent = WarehouseRent.objects.all() 
    furnished_apartements_rent = FurnishedApartmentRent.objects.all() 
    chalets_rent = ChaletRent.objects.all() 


    context = {
        'apartments_rent': apartments_rent,
        'floors_rent': floors_rent, 
        'villas_rent': villas_rent, 
        'shops_rent': shops_rent, 
        'resthouses_rent': resthouses_rent, 
        'commercial_offices_rent': commercial_offices_rent, 
        'lands_rent': lands_rent, 
        'buildings_rent': buildings_rent, 
        'warehouses_rent': warehouses_rent, 
        'furnished_apartements_rent': furnished_apartements_rent, 
        'chalets_rent': chalets_rent 
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


def ad_uploaded(request): 
    context = {} 
    return render(request, 'pages/ad-uploaded-successfully.html', context)
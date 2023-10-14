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
    ### variables to get from html template 
    # price 
    # space 
    # advertiser_relation 
    # exclusive 
    # street width 
    # room count 
    # lounges
    # bathrooms 
    # floor 
    # property_age 

    exclusive = 0 

    if request.POST: 
        title = request.POST.get('title-input') 
        price = request.POST.get('price-input') 
        space = request.POST.get('space-input') 
        advertiser_relation = request.POST.get('advertiser_relation')
        if advertiser_relation != "مسوق": 
            exclusive = 0  
        else: 
            exclusive = request.POST.get('exclusive') 
        imgs = request.FILES.get('property__imgs')
        video = request.FILES.get('property__video')
        lat = request.POST.get('lat') 
        lng = request.POST.get('lng') 
        rooms = request.POST.get('room-input') 
        lounges = request.POST.get('lounges-input') 
        bathrooms = request.POST.get('bathroom-input') 
        floor = request.POST.get('floor-input') 
        property_age = request.POST.get('property-age-input') 
        description = request.POST.get('property__description__input') 
        rent_type_input = request.POST.get('rent_type_input') 
        
        families = request.POST.get('families') 
        furnished = request.POST.get('furnished') 
        kitchen = request.POST.get('kitchen') 
        extenstion = request.POST.get('extenstion') 
        car_entrance = request.POST.get('car_entrance') 
        elevator = request.POST.get('elevator') 
        ac = request.POST.get('ac') 
        water_exist = request.POST.get('water_exist') 
        power_exist = request.POST.get('power_exist')         
        sanitation_exist = request.POST.get('sanitation_exist') 
        private_surface = request.POST.get('private_surface') 
        in_villa = request.POST.get('in_villa') 
        two_enternace = request.POST.get('two_enternace') 
        private_enternace = request.POST.get('private_enternace') 

        features = [
            families, 
            furnished, 
            kitchen, extenstion, 
            car_entrance, 
            elevator, 
            ac, 
            water_exist,
            power_exist, 
            sanitation_exist, 
            private_surface, in_villa, two_enternace, private_enternace
        ]


        for i in range(len(features)): 
            if features[i] == 'on': 
                features[i] = 1 
            else: 
                features[i] = 0 
        


        apartment = ApartmentRent.objects.create(
            title= title, 
            description = description, 
            price= price, 
            space=space, 
            advertiser_relation= advertiser_relation, 
            exclusive = exclusive, 
            rooms = rooms, 
            lounges = lounges, 
            bathroom = bathrooms, 
            floor = floor , 
            property_age = property_age, 
            rent_type = rent_type_input, 
            lat = lat, 
            lng=lng ,
            families = features[0], 
            furnished = features[1], 
            kitchen = features[2], 
            extenstion = features[3], 
            car_entrance = features[4], 
            elevator = features[5], 
            ac = features[6] , 
            water_exist = features[7], 
            power_exist = features[8], 
            sanitation_exist = features[9], 
            private_surface = features[10], 
            in_villa = features[11], 
            two_enternace = features[12], 
            private_enternace = features[13]
        ) 
        

        # print(price)
        # print(space)
        # print(advertiser_relation)
        # print(exclusive)
        # print(imgs)
        # print(video)
        # print(lat)
        # print(lng)
        # print(rooms)
        # print(lounges)
        # print(bathrooms)
        # print(floor)
        # print(property_age)

    context = {} 
    return render(request, 'property/add-apartment-rent.html', context)
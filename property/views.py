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
        price = request.POST.get('price-input') 
        space = request.POST.get('space-input') 
        street_width = request.POST.get('street-width-input') 
        advertiser_relation = request.POST.get('advertiser_relation')
        if advertiser_relation != "مسوق": 
            exclusive = 0  
        else: 
            exclusive = request.POST.get('exclusive') 
        imgs = request.FILES.get('property__imgs')
        video = request.FILES.get('property__video')
        lat = request.POST.get('lat') 
        lng = request.POST.get('lng') 
        # rooms = request.POST.get('room-input') 
        # if rooms == "" or rooms == 0 or rooms == None: 
        rooms = request.POST.get('extra-room-input') 
        if rooms == None or rooms == "" or rooms == 0: 
            rooms = request.POST.get("room-input")  
        
        
        lounges = request.POST.get('extra-lounges-input') 
        if lounges == None or lounges == "" or lounges == 0: 
            lounges = request.POST.get('lounges-input') 
        

        bathrooms = request.POST.get('extra-bathroom-input') 
        if bathrooms == None or bathrooms == '' or bathrooms == 0 : 
            bathrooms = request.POST.get('bathroom-input') 


        floor = request.POST.get('extra-floor-input') 
        if floor == None or floor == '' or floor == 0: 
            floor = request.POST.get('floor-input') 


        property_age = request.POST.get('extra-property-age-input') 
        if property_age == None or property_age == '' or property_age == 0: 
            property_age = request.POST.get('property-age-input') 
        
        description = request.POST.get('property__description__input') 
        rent_type_input = request.POST.get('rent_type_input') 
        try: 
            video = request.FILES['property__video'] 
        except: 
            video = None 
        print(video) 
        images = request.FILES.getlist('property__imgs') 
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
            street_width= street_width, 
            description = description, 
            price= price, 
            space=space, 
            video= video, 
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

        for img in images: 
            ApartmentRentImage.objects.create(
                ad = apartment, 
                img = img
            ).save() 
            

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



def add_floor_rent(request): 
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
        price = request.POST.get('price-input') 
        space = request.POST.get('space-input') 
        street_width = request.POST.get('street-width-input') 
        advertiser_relation = request.POST.get('advertiser_relation')
        if advertiser_relation != "مسوق": 
            exclusive = 0  
        else: 
            exclusive = request.POST.get('exclusive') 
        imgs = request.FILES.get('property__imgs')
        video = request.FILES.get('property__video')
        lat = request.POST.get('lat') 
        lng = request.POST.get('lng') 
        # rooms = request.POST.get('room-input') 
        # if rooms == "" or rooms == 0 or rooms == None: 
        rooms = request.POST.get('extra-room-input') 
        if rooms == None or rooms == "" or rooms == 0: 
            rooms = request.POST.get("room-input")  
        
        
        lounges = request.POST.get('extra-lounges-input') 
        if lounges == None or lounges == "" or lounges == 0: 
            lounges = request.POST.get('lounges-input') 
        

        bathrooms = request.POST.get('extra-bathroom-input') 
        if bathrooms == None or bathrooms == '' or bathrooms == 0 : 
            bathrooms = request.POST.get('bathroom-input') 


        floor = request.POST.get('extra-floor-input') 
        if floor == None or floor == '' or floor == 0: 
            floor = request.POST.get('floor-input') 


        property_age = request.POST.get('extra-property-age-input') 
        if property_age == None or property_age == '' or property_age == 0: 
            property_age = request.POST.get('property-age-input') 
        
        description = request.POST.get('property__description__input') 
        rent_type_input = request.POST.get('rent_type_input') 
        try: 
            video = request.FILES['property__video'] 
        except: 
            video = None 
        print(video) 
        images = request.FILES.getlist('property__imgs') 
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
        


        floor = FloorRent.objects.create(
            street_width= street_width, 
            description = description, 
            price= price, 
            space=space, 
            video= video, 
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

        for img in images: 
            FloorRentImage.objects.create(
                ad = floor, 
                img = img
            ).save() 
            

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
    return render(request, 'property/add-floor-rent.html', context)



def add_villa_rent(request): 
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
        price = request.POST.get('price-input') 
        space = request.POST.get('space-input') 
        street_width = request.POST.get('street-width-input') 
        advertiser_relation = request.POST.get('advertiser_relation')
        if advertiser_relation != "مسوق": 
            exclusive = 0  
        else: 
            exclusive = request.POST.get('exclusive') 
        imgs = request.FILES.get('property__imgs')
        video = request.FILES.get('property__video')
        lat = request.POST.get('lat') 
        lng = request.POST.get('lng') 
        # rooms = request.POST.get('room-input') 
        # if rooms == "" or rooms == 0 or rooms == None: 
        rooms = request.POST.get('extra-room-input') 
        if rooms == None or rooms == "" or rooms == 0: 
            rooms = request.POST.get("room-input")  
        
        
        lounges = request.POST.get('extra-lounges-input') 
        if lounges == None or lounges == "" or lounges == 0: 
            lounges = request.POST.get('lounges-input') 
        

        bathrooms = request.POST.get('extra-bathroom-input') 
        if bathrooms == None or bathrooms == '' or bathrooms == 0 : 
            bathrooms = request.POST.get('bathroom-input') 


        floor = request.POST.get('extra-floor-input') 
        if floor == None or floor == '' or floor == 0: 
            floor = request.POST.get('floor-input') 


        property_age = request.POST.get('extra-property-age-input') 
        if property_age == None or property_age == '' or property_age == 0: 
            property_age = request.POST.get('property-age-input') 
        
        description = request.POST.get('property__description__input') 
        rent_type_input = request.POST.get('rent_type_input') 
        try: 
            video = request.FILES['property__video'] 
        except: 
            video = None 
        print(video) 
        images = request.FILES.getlist('property__imgs') 
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
        driver_room = request.POST.get('driver_room') 
        maid_room = request.POST.get("maid_room") 
        duplex = request.POST.get("duplex") 
        yard = request.POST.get("yard") 
        hair_tent_house = request.POST.get('hair_tent_house') 


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
            private_surface, in_villa, two_enternace, private_enternace, 
            driver_room, 
            maid_room, 
            duplex, 
            yard, 
            hair_tent_house
        ]


        for i in range(len(features)): 
            if features[i] == 'on': 
                features[i] = 1 
            else: 
                features[i] = 0 
        


        villa = VillaRent.objects.create(
            street_width= street_width, 
            description = description, 
            price= price, 
            space=space, 
            video= video, 
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
            private_enternace = features[13], 
            driver_room= features[14],
            maid_room = features[15], 
            duplex = features[16] , 
            yard = features[17], 
            hair_tent_house = features[18]
        )

        for img in images: 
            VillaRentImage.objects.create(
                ad = villa, 
                img = img
            ).save() 
            

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
    return render(request, 'property/add-villa-rent.html', context)



def add_shop_rent(request): 
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
        price = request.POST.get('price-input') 
        space = request.POST.get('space-input') 
        street_width = request.POST.get('street-width-input') 
        advertiser_relation = request.POST.get('advertiser_relation')
        if advertiser_relation != "مسوق": 
            exclusive = 0  
        else: 
            exclusive = request.POST.get('exclusive') 
        imgs = request.FILES.get('property__imgs')
        video = request.FILES.get('property__video')
        lat = request.POST.get('lat') 
        lng = request.POST.get('lng') 

        

        description = request.POST.get('property__description__input') 
        # rent_type_input = request.POST.get('rent_type_input') 
        try: 
            video = request.FILES['property__video'] 
        except: 
            video = None 
        print(video) 
        images = request.FILES.getlist('property__imgs') 
        # families = request.POST.get('families') 
        # furnished = request.POST.get('furnished') 
        # kitchen = request.POST.get('kitchen') 
        # extenstion = request.POST.get('extenstion') 
        # car_entrance = request.POST.get('car_entrance') 
        # elevator = request.POST.get('elevator') 
        # ac = request.POST.get('ac') 
        water_exist = request.POST.get('water_exist') 
        power_exist = request.POST.get('power_exist')         
        sanitation_exist = request.POST.get('sanitation_exist') 
        # private_surface = request.POST.get('private_surface') 
        # in_villa = request.POST.get('in_villa') 
        # two_enternace = request.POST.get('two_enternace') 
        # private_enternace = request.POST.get('private_enternace') 

        features = [
            # families, 
            # furnished, 
            # kitchen, extenstion, 
            # car_entrance, 
            # elevator, 
            # ac, 
            water_exist,
            power_exist, 
            sanitation_exist, 
            # private_surface, in_villa, tw`o_enternace, private_enternace
        ]


        for i in range(len(features)): 
            if features[i] == 'on': 
                features[i] = 1 
            else: 
                features[i] = 0 
        


        shop = ShopRent.objects.create(
            street_width= street_width, 
            description = description, 
            price= price, 
            space=space, 
            video= video, 
            advertiser_relation= advertiser_relation, 
            exclusive = exclusive, 
            # rooms = rooms, 
            # lounges = lounges, 
            # bathroom = bathrooms, 
            # floor = floor , 
            # property_age = property_age, 
            # rent_type = rent_type_input, 
            lat = lat, 
            lng=lng ,
            # families = features[0], 
            # furnished = features[1], 
            # kitchen = features[2], 
            # extenstion = features[3], 
            # car_entrance = features[4], 
            # elevator = features[5], 
            # ac = features[6] , 
            water_exist = features[0], 
            power_exist = features[1], 
            sanitation_exist = features[2], 
            # private_surface = features[10], 
            # in_villa = features[11], 
            # two_enternace = features[12], 
            # private_enternace = features[13]
        )

        for img in images: 
            ShopRentImage.objects.create(
                ad = shop, 
                img = img
            ).save() 
            

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
    return render(request, 'property/add-shop-rent.html', context)



def add_rest_house_rent(request): 


    exclusive = 0 

    if request.POST: 
        price = request.POST.get('price-input') 
        space = request.POST.get('space-input') 
        street_width = request.POST.get('street-width-input') 
        advertiser_relation = request.POST.get('advertiser_relation')
        if advertiser_relation != "مسوق": 
            exclusive = 0  
        else: 
            exclusive = request.POST.get('exclusive') 
        imgs = request.FILES.get('property__imgs')
        video = request.FILES.get('property__video')
        lat = request.POST.get('lat') 
        lng = request.POST.get('lng') 
        # rooms = request.POST.get('room-input') 
        # if rooms == "" or rooms == 0 or rooms == None: 
        rooms = request.POST.get('extra-room-input') 
        if rooms == None or rooms == "" or rooms == 0: 
            rooms = request.POST.get("room-input")  
        
        
        lounges = request.POST.get('extra-lounges-input') 
        if lounges == None or lounges == "" or lounges == 0: 
            lounges = request.POST.get('lounges-input') 
        

        bathrooms = request.POST.get('extra-bathroom-input') 
        if bathrooms == None or bathrooms == '' or bathrooms == 0 : 
            bathrooms = request.POST.get('bathroom-input') 


        floor = request.POST.get('extra-floor-input') 
        if floor == None or floor == '' or floor == 0: 
            floor = request.POST.get('floor-input') 


        property_age = request.POST.get('extra-property-age-input') 
        if property_age == None or property_age == '' or property_age == 0: 
            property_age = request.POST.get('property-age-input') 
        
        description = request.POST.get('property__description__input') 
        rent_type_input = request.POST.get('rent_type_input') 
        try: 
            video = request.FILES['property__video'] 
        except: 
            video = None 
        print(video) 
        images = request.FILES.getlist('property__imgs') 
        kitchen = request.POST.get('kitchen')
        water_exist = request.POST.get('water_exist') 
        power_exist = request.POST.get('power_exist')         
        sanitation_exist = request.POST.get('sanitation_exist') 
        pool = request.POST.get('pool')
        football_field = request.POST.get('football_field') 
        volly_field = request.POST.get('volly_field') 
        hair_tent_house = request.POST.get('hair_tent_house')
        amusement = request.POST.get('amusement') 
        family_part = request.POST.get('family_part') 


        features = [
            kitchen,
            water_exist,
            power_exist,
            sanitation_exist,
            pool,
            football_field,
            volly_field,
            hair_tent_house,
            amusement,
            family_part
        ]

        for i in range(len(features)): 
            if features[i] == 'on': 
                features[i] = 1 
            else: 
                features[i] = 0 
        


        rest_house = RestHouseRent.objects.create(
            street_width= street_width, 
            description = description, 
            price= price, 
            space=space, 
            video= video, 
            advertiser_relation= advertiser_relation, 
            exclusive = exclusive, 
            rooms = rooms, 
            lounges = lounges, 
            bathroom = bathrooms, 
            # floor = floor , 
            property_age = property_age, 
            rent_type = rent_type_input, 
            lat = lat, 
            lng=lng ,

            kitchen = features[0],
            water_exist = features[1],
            power_exist = features[2],
            sanitation_exist = features[3],
            pool = features[4],
            football_field= features[5],
            volly_field = features[6],
            hair_tent_house =features[7],
            amusement = features[8],
            family_part = features[9]
        )

        for img in images: 
            RestHouseRentImage.objects.create(
                ad = rest_house, 
                img = img
            ).save() 
            


    context = {} 
    return render(request, 'property/add-rest-house-rent.html', context)



def add_building_rent(request): 

    exclusive = 0 

    if request.POST: 
        price = request.POST.get('price-input') 
        space = request.POST.get('space-input') 
        street_width = request.POST.get('street-width-input') 
        advertiser_relation = request.POST.get('advertiser_relation')
        if advertiser_relation != "مسوق": 
            exclusive = 0  
        else: 
            exclusive = request.POST.get('exclusive') 
        imgs = request.FILES.get('property__imgs')
        video = request.FILES.get('property__video')
        lat = request.POST.get('lat') 
        lng = request.POST.get('lng') 
        store_count = request.POST.get('stores-count-input') 
        rooms = request.POST.get('extra-room-input') 
        if rooms == None or rooms == "" or rooms == 0: 
            rooms = request.POST.get("room-input")  
        

        apartments_count = request.POST.get('extra-apartments-count-input') 
        if apartments_count == None or apartments_count == "" or apartments_count == 0: 
            apartments_count = request.POST.get('property-apartments-count')


        property_age = request.POST.get('extra-property-age-input') 
        if property_age == None or property_age == '' or property_age == 0: 
            property_age = request.POST.get('property-age-input') 
        
        description = request.POST.get('property__description__input') 
        rent_type_input = request.POST.get('rent_type_input') 
        try: 
            video = request.FILES['property__video'] 
        except: 
            video = None 
        print(video) 
        images = request.FILES.getlist('property__imgs') 
        furnished = request.POST.get('furnished') 

        water_exist = request.POST.get('water_exist') 
        power_exist = request.POST.get('power_exist')         
        sanitation_exist = request.POST.get('sanitation_exist') 


        features = [
            furnished,
            water_exist,
            power_exist,
            sanitation_exist,
        ]


        for i in range(len(features)): 
            if features[i] == 'on': 
                features[i] = 1 
            else: 
                features[i] = 0 
        


        building = BuildingRent.objects.create(
            street_width= street_width, 
            description = description, 
            price= price, 
            space=space, 
            video= video, 
            advertiser_relation= advertiser_relation, 
            exclusive = exclusive, 
            rooms = rooms, 
            property_age = property_age, 
            rent_type = rent_type_input, 
            lat = lat, 
            lng=lng ,
            sotres_count = store_count, 
            furnished = features[0],
            water_exist = features[1],
            power_exist = features[2],
            sanitation_exist = features[3],
            
        )

        for img in images: 
            BuildingRentImage.objects.create(
                ad = building, 
                img = img
            ).save() 


    context = {} 
    return render(request, 'property/add-building-rent.html', context)



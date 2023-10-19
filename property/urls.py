from django.urls import path 
from .views import * 

app_name = 'property' 

urlpatterns = [
    path('<str:number>/details/', property_details, name='property-details'), 
    path('add-property/', add_property, name='add-property'), 
    path('add-property/rent/apartment/', add_apartment_rent, name='add-apartment-rent'), 
    path('add-property/rent/floor/', add_floor_rent, name='add-floor-rent'),  
    path('add-property/rent/villa/', add_villa_rent, name='add-villa-rent'),  
    path('add-property/rent/shop/', add_shop_rent, name='add-shop-rent'),  
    path('add-property/rent/rest-house/', add_rest_house_rent, name='add-rest-house-rent'),  
]
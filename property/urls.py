from django.urls import path 
from .views import * 

app_name = 'property' 

urlpatterns = [
    path('<str:number>/details/', property_details, name='property-details'), 
    path('add-property/', add_property, name='add-property'), 
    path('add-property/rent/apartment/', add_apartment_rent, name='add-apartment-rent'),  
]
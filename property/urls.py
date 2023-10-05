from django.urls import path 
from .views import * 

app_name = 'property' 

urlpatterns = [
    path('<str:number>/details/', property_details, name='property-details') 
]
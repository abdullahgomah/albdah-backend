from django.urls import path 
from .views import * 

app_name = 'property' 

urlpatterns = [
    path('details/', property_details, name='property-details') 
]
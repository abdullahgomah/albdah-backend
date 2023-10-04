from django.urls import path 
from .views import * 

app_name = 'pages'

urlpatterns = [
    path('', home, name='home'), 
    path('about/', about, name='about'), 
    path('contact/', contact, name='contact'), 
    path('request-contract/', request_contract, name='request-contract'), 
]
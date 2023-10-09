from django.contrib import admin
from .models import * 
# Register your models here.


admin.site.register(ApartmentRent) 
admin.site.register(ApartmentRentImage) 

admin.site.register(FloorRent)
admin.site.register(FloorRentImage)

admin.site.register(VillaRent)
admin.site.register(VillaRentImage)


admin.site.register(ShopRent)
admin.site.register(ShopRentImage)



admin.site.register(RestHouseRent)
admin.site.register(RestHouseRentImage)

admin.site.register(CommercialOfficeRent)
admin.site.register(CommercialOfficeRentImage)


admin.site.register(LandRent)
admin.site.register(LandRentImage)


admin.site.register(BuildingRent)
admin.site.register(BuildingRentImage)



admin.site.register(Purpose) 

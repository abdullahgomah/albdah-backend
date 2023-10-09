from django.db import models
from geoposition.fields import GeopositionField
import random 
import string 

# Create your models here.


RENT_TYPE_CHOICES = [
    ('yearly', "سنوي"),
    ('monthly', "شهري")
]


INTERFACE_CHOICES = [
    ('شمالية', 'شمالية'),
    ('جنوبية', 'جنوبية'),
    ('غربية', 'غربية'),
    ('شرقية', 'شرقية'),
    ('شمالية شرقية', 'شمالية شرقية'),
    ('شمالية غربية', 'شمالية غربية'),
    ('جنوبية شرقية', 'جنوبية شرقية'),
    ('جنوبية غربية', 'جنوبية غربية')
]


def generate(): 
    # Generate 2 random numbers between 0 and 9
    random_numbers = ''.join(random.choice(string.digits) for _ in range(2))

# Generate 3 random characters (uppercase and lowercase letters)
    random_characters = ''.join(random.choice(string.ascii_letters) for _ in range(3))

# Combine the random numbers and characters
    random_value = random_numbers + random_characters

    return str(random_value) 

#### شقة 

class ApartmentRent(models.Model): 
    number = models.CharField(max_length=20, verbose_name="رقم الإعلان", null=True, blank=True)  
    position = GeopositionField() 

    title = models.CharField(max_length=200, verbose_name="عنوان الإعلان", null=True, blank=True) 

    price = models.IntegerField(verbose_name="السعر (ريال سعودي)", default=0) 
    space = models.IntegerField(verbose_name="المساحة (متر مربع)", default=0) 
    width = models.FloatField(verbose_name="العرض (متر)") 
    length = models.FloatField(verbose_name="الطول (متر)")

    advertiser_relation = models.CharField(max_length=50, verbose_name="علاقة المعلن بالعقار")
    exclusive = models.BooleanField(default=False, verbose_name='حصري') 


    video = models.FileField(upload_to='rent/apartment/video', verbose_name="فيديو")

    street_width = models.FloatField(verbose_name="عرض الشارع") 
    rooms = models.IntegerField(default=0, verbose_name="الغرف") 

    lounges = models.IntegerField(default=0, verbose_name="الصالات") 

    bathroom = models.IntegerField(default=0, verbose_name="عدد دورات المياه") 

    floor = models.IntegerField(default=0, verbose_name="الدور") 

    property_age = models.IntegerField(default=0, verbose_name="عمر العقار") 

    families = models.BooleanField(default=True, verbose_name="عوائل ام عزاب") 

    rent_type = models.CharField(max_length=50, choices=RENT_TYPE_CHOICES, verbose_name="نوع الإيجار") 


    description = models.TextField(verbose_name="وصف العقار", default="   ")

    furnished = models.BooleanField(default=False, verbose_name="مؤثثة") 

    kitchen = models.BooleanField(default=False, verbose_name="مطبخ")

    extenstion = models.BooleanField(default=False, verbose_name="ملحق")

    car_entrance= models.BooleanField(default=False, verbose_name="مدخل سيارة")

    elevator = models.BooleanField(default=False, verbose_name="مصعد كهربائي") 
    
    ac = models.BooleanField(default=False, verbose_name="مكيف")

    water_exist = models.BooleanField(default=False, verbose_name="توفر الماء")
    power_exist = models.BooleanField(default=False, verbose_name="توفر الكهرباء")
    sanitation_exist = models.BooleanField(default=False, verbose_name="توفر الصرف")

    private_surface =models.BooleanField(default=False, verbose_name="سطح خاص")

    in_villa = models.BooleanField(default=False, verbose_name="في فيلا")
    two_enternace = models.BooleanField(default=False, verbose_name="مدخلين")

    private_enternace = models.BooleanField(default=False, verbose_name="مدخل خاص")

    def __str__(self): 
        return self.title 
    

    def save(self, *args, **kwargs): 
        if not self.number: 
            self.number = generate()
        super(ApartmentRent, self).save(*args, **kwargs)

class ApartmentRentImage(models.Model):
    ad = models.ForeignKey(ApartmentRent, on_delete=models.CASCADE, verbose_name="الإعلان", related_name='imgs') 
    img = models.ImageField(upload_to="rent/apartment/")
    
    def __str__(self):
        return str(self.ad ) 






####### دور 

class FloorRent(models.Model):

    number = models.CharField(max_length=20, verbose_name="رقم الإعلان", null=True, blank=True)  
    position = GeopositionField() 
    title = models.CharField(max_length=200, verbose_name="عنوان الإعلان", null=True, blank=True) 

    

    price = models.IntegerField(verbose_name="السعر (ريال سعودي)", default=0) 
    space = models.IntegerField(verbose_name="المساحة (متر مربع)", default=0) 
    width = models.FloatField(verbose_name="العرض (متر)") 
    length = models.FloatField(verbose_name="الطول (متر)")

    advertiser_relation = models.CharField(max_length=50, verbose_name="علاقة المعلن بالعقار")
    exclusive = models.BooleanField(default=False, verbose_name='حصري') 


    video = models.FileField(upload_to='rent/floor/video', verbose_name="فيديو")

    street_width = models.FloatField(verbose_name="عرض الشارع") 
    rooms = models.IntegerField(default=0) 

    lounges = models.IntegerField(default=0, verbose_name="الصالات") 

    bathroom = models.IntegerField(default=0, verbose_name="عدد دورات المياه") 

    floor = models.IntegerField(default=0, verbose_name="الدور") 

    property_age = models.IntegerField(default=0, verbose_name="عمر العقار") 

    families = models.BooleanField(default=True, verbose_name="عوائل ام عزاب") 

    rent_type = models.CharField(max_length=50, choices=RENT_TYPE_CHOICES, verbose_name="نوع الإيجار") 


    description = models.TextField(verbose_name="وصف العقار")

    furnished = models.BooleanField(default=False, verbose_name="مؤثثة") 

    kitchen = models.BooleanField(default=False, verbose_name="مطبخ")

    extenstion = models.BooleanField(default=False, verbose_name="ملحق")

    car_entrance= models.BooleanField(default=False, verbose_name="مدخل سيارة")

    elevator = models.BooleanField(default=False, verbose_name="مصعد كهربائي") 
    
    ac = models.BooleanField(default=False, verbose_name="مكيف")

    water_exist = models.BooleanField(default=False, verbose_name="توفر الماء")
    power_exist = models.BooleanField(default=False, verbose_name="توفر الكهرباء")
    sanitation_exist = models.BooleanField(default=False, verbose_name="توفر الصرف")

    private_surface =models.BooleanField(default=False, verbose_name="سطح خاص")

    in_villa = models.BooleanField(default=False, verbose_name="في فيلا")
    two_enternace = models.BooleanField(default=False, verbose_name="مدخلين")

    private_enternace = models.BooleanField(default=False, verbose_name="مدخل خاص")



    def save(self, *args, **kwargs): 
        if not self.number: 
            self.number = generate()
        super(FloorRent, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'FloorRent'
        verbose_name_plural = 'FloorRents'


class FloorRentImage(models.Model):
    ad = models.ForeignKey(FloorRent, on_delete=models.CASCADE, verbose_name="الإعلان") 
    img = models.ImageField(upload_to="rent/floor/")
    
    def __str__(self):
        return " "






##### فيلا 

class VillaRent(models.Model):
    number = models.CharField(max_length=20, verbose_name="رقم الإعلان", null=True, blank=True)  
    position = GeopositionField() 
    title = models.CharField(max_length=200, verbose_name="عنوان الإعلان", null=True, blank=True) 

    interface = models.CharField(max_length=100, verbose_name="الواجهة", choices=INTERFACE_CHOICES) 


    price = models.IntegerField(verbose_name="السعر (ريال سعودي)", default=0) 
    space = models.IntegerField(verbose_name="المساحة (متر مربع)", default=0) 
    width = models.FloatField(verbose_name="العرض (متر)") 
    length = models.FloatField(verbose_name="الطول (متر)")

    advertiser_relation = models.CharField(max_length=50, verbose_name="علاقة المعلن بالعقار")
    exclusive = models.BooleanField(default=False, verbose_name='حصري') 


    video = models.FileField(upload_to='rent/villa/video', verbose_name="فيديو")

    street_width = models.FloatField(verbose_name="عرض الشارع") 
    rooms = models.IntegerField(default=0) 

    lounges = models.IntegerField(default=0, verbose_name="الصالات") 

    bathroom = models.IntegerField(default=0, verbose_name="عدد دورات المياه") 

    floor = models.IntegerField(default=0, verbose_name="الدور") 

    property_age = models.IntegerField(default=0, verbose_name="عمر العقار") 

    families = models.BooleanField(default=True, verbose_name="عوائل ام عزاب") 

    rent_type = models.CharField(max_length=50, choices=RENT_TYPE_CHOICES, verbose_name="نوع الإيجار") 


    description = models.TextField(verbose_name="وصف العقار")

    furnished = models.BooleanField(default=False, verbose_name="مؤثثة") 

    kitchen = models.BooleanField(default=False, verbose_name="مطبخ")

    extenstion = models.BooleanField(default=False, verbose_name="ملحق")

    car_entrance= models.BooleanField(default=False, verbose_name="مدخل سيارة")

    elevator = models.BooleanField(default=False, verbose_name="مصعد كهربائي") 
    
    ac = models.BooleanField(default=False, verbose_name="مكيف")

    water_exist = models.BooleanField(default=False, verbose_name="توفر الماء")
    power_exist = models.BooleanField(default=False, verbose_name="توفر الكهرباء")
    sanitation_exist = models.BooleanField(default=False, verbose_name="توفر الصرف")

    private_surface =models.BooleanField(default=False, verbose_name="سطح خاص")

    in_villa = models.BooleanField(default=False, verbose_name="في فيلا")
    two_enternace = models.BooleanField(default=False, verbose_name="مدخلين")

    private_enternace = models.BooleanField(default=False, verbose_name="مدخل خاص")

    driver_room = models.BooleanField(default=False, verbose_name="غرفة سائق") 
    maid_room = models.BooleanField(default=False, verbose_name="غرفة خادمة")

    duplex = models.BooleanField(default=False, verbose_name='دوبلكس')

    basement = models.BooleanField(default=False, verbose_name="قبو") 

    yard = models.BooleanField(default=False, verbose_name="حوش") 

    hair_tent_house = models.BooleanField(default=False, verbose_name="بيت شعر")



    def save(self, *args, **kwargs): 
        if not self.number: 
            self.number = generate()
        super(VillaRent, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'VillaRent'
        verbose_name_plural = 'VillaRents'





class VillaRentImage(models.Model):
    ad = models.ForeignKey(VillaRent, on_delete=models.CASCADE, verbose_name="الإعلان") 
    img = models.ImageField(upload_to="rent/villa/")
    
    def __str__(self):
        return " "


####### محل

class ShopRent(models.Model):
    number = models.CharField(max_length=20, verbose_name="رقم الإعلان", null=True, blank=True)  
    position = GeopositionField() 
    title = models.CharField(max_length=200, verbose_name="عنوان الإعلان", null=True, blank=True) 

    
    interface = models.CharField(max_length=100, verbose_name="الواجهة", choices=INTERFACE_CHOICES, null=True, blank=True) 

    street_width = models.IntegerField(default=0, verbose_name="عرض الشارع")

    property_age = models.IntegerField(default=0, verbose_name="عمر العقار")


    description = models.TextField(verbose_name="وصف العقار", null=True, blank=True)

    water_exist = models.BooleanField(default=False, verbose_name="توفر الماء")
    power_exist = models.BooleanField(default=False, verbose_name="توفر الكهرباء")
    sanitation_exist = models.BooleanField(default=False, verbose_name="توفر الصرف")

    video = models.FileField(upload_to="rent/shop_rent/", verbose_name="فيديو", null=True, blank=True)


    def save(self, *args, **kwargs): 
        if not self.number: 
            self.number = generate()
        super(ShopRent, self).save(*args, **kwargs)


    def __str__(self):
        pass

    class Meta:
        verbose_name = 'ShopRent'
        verbose_name_plural = 'ShopRents'



class ShopRentImage(models.Model):
    ad = models.ForeignKey(ShopRent, on_delete=models.CASCADE, verbose_name="الإعلان") 
    img = models.ImageField(upload_to="rent/shop_rent/")
    
    def __str__(self):
        return " "






####### استراحة

class RestHouseRent(models.Model):
    number = models.CharField(max_length=20, verbose_name="رقم الإعلان", null=True, blank=True)  
    position = GeopositionField() 
    title = models.CharField(max_length=200, verbose_name="عنوان الإعلان", null=True, blank=True) 

    street_width = models.IntegerField(default=0, verbose_name="عرض الشارع")
    property_age = models.IntegerField(default=0, verbose_name="عمر العقار")
    lounges = models.IntegerField(default=0, verbose_name="الصالات") 
    rooms = models.IntegerField(default=0, verbose_name="الغرف")
    bathroom = models.IntegerField(default=0, verbose_name="عدد دورات المياه") 

    description = models.TextField(verbose_name="وصف العقار", null=True, blank=True)
    pool = models.BooleanField(default=False, verbose_name="مسبح")
    football_field = models.BooleanField(default=False, verbose_name="ملعب كرة قدم")
    volly_field = models.BooleanField(default=False, verbose_name="ملعب كرة طائرة")

    hair_tent_house = models.BooleanField(default=False, verbose_name="بيت شعر")

    kitchen = models.BooleanField(default=False, verbose_name="مطبخ")

    amusement = models.BooleanField(default=False, verbose_name="ملاهي")

    family_part = models.BooleanField(default=False, verbose_name="قسم عوائل")

    water_exist = models.BooleanField(default=False, verbose_name="توفر الماء")
    power_exist = models.BooleanField(default=False, verbose_name="توفر الكهرباء")
    sanitation_exist = models.BooleanField(default=False, verbose_name="توفر الصرف")

    video = models.FileField(upload_to='rent/rest_house/video', verbose_name="فيديو", null=True, blank=True)


    def save(self, *args, **kwargs): 
        if not self.number: 
            self.number = generate()
        super(RestHouseRent, self).save(*args, **kwargs)


    def __str__(self):
        pass

    class Meta:
        verbose_name = 'RestHouseRent'
        verbose_name_plural = 'RestHouseRents'




class RestHouseRentImage(models.Model):
    ad = models.ForeignKey(RestHouseRent, on_delete=models.CASCADE, verbose_name="الإعلان") 
    img = models.ImageField(upload_to="rent/rest_house/")
    
    def __str__(self):
        return " "




######## مكتب تجاري

class CommercialOfficeRent(models.Model):
    number = models.CharField(max_length=20, verbose_name="رقم الإعلان", null=True, blank=True)  
    position = GeopositionField() 
    title = models.CharField(max_length=200, verbose_name="عنوان الإعلان", null=True, blank=True) 

    street_width = models.IntegerField(default=0, verbose_name="عرض الشارع")
    floor = models.IntegerField(default=False, verbose_name="الدور")
    rooms = models.IntegerField(default=0, verbose_name="الغرف") 
    lounges = models.IntegerField(default=0, verbose_name="الصالات") 
    bathroom = models.IntegerField(default=0, verbose_name="عدد دورات المياه") 
    property_age = models.IntegerField(default=0, verbose_name="عمر العقار") 
    description = models.TextField(verbose_name="وصف العقار", null=True, blank=True)

    furnished = models.BooleanField(default=False, verbose_name="مؤثثة") 
    
    water_exist = models.BooleanField(default=False, verbose_name="توفر الماء")
    power_exist = models.BooleanField(default=False, verbose_name="توفر الكهرباء")
    sanitation_exist = models.BooleanField(default=False, verbose_name="توفر الصرف")

    video = models.FileField(upload_to='rent/commercial_office/video', verbose_name="فيديو", null=True, blank=True)

    def save(self, *args, **kwargs): 
        if not self.number: 
            self.number = generate()
        super(CommercialOfficeRent, self).save(*args, **kwargs)




    class Meta:
        verbose_name = 'CommercialOfficeRent'
        verbose_name_plural = 'CommercialOfficeRents'





class CommercialOfficeRentImage(models.Model):
    ad = models.ForeignKey(CommercialOfficeRent, on_delete=models.CASCADE, verbose_name="الإعلان") 
    img = models.ImageField(upload_to="rent/commercial_office/")




#### الأغراض 

class Purpose(models.Model): 
    name= models.CharField(max_length=200, verbose_name="الاسم")

    def __str__(self):
        return self.name 

#######  أرض 
class LandRent(models.Model):
    number = models.CharField(max_length=20, verbose_name="رقم الإعلان", null=True, blank=True)  
    position = GeopositionField() 
    title = models.CharField(max_length=200, verbose_name="عنوان الإعلان", null=True, blank=True) 

    interface = models.CharField(max_length=100, verbose_name="الواجهة", choices=INTERFACE_CHOICES, null=True, blank=True) 
    street_width = models.FloatField(verbose_name="عرض الشارع", null=True, blank=True) 
    
    purpose = models.ForeignKey(Purpose, on_delete=models.SET_NULL, null=True, blank=True) 
    description = models.TextField(verbose_name="وصف العقار", default="  ")

    water_exist = models.BooleanField(default=False, verbose_name="توفر الماء")
    power_exist = models.BooleanField(default=False, verbose_name="توفر الكهرباء")
    sanitation_exist = models.BooleanField(default=False, verbose_name="توفر الصرف")
    video = models.FileField(upload_to='rent/land/video', verbose_name="فيديو", null=True, blank=True)


    def save(self, *args, **kwargs): 
        if not self.number: 
            self.number = generate()
        super(LandRent, self).save(*args, **kwargs)



    class Meta:
        verbose_name = 'LandRent'
        verbose_name_plural = 'LandRents'


class LandRentImage(models.Model):
    ad = models.ForeignKey(LandRent, on_delete=models.CASCADE, verbose_name="الإعلان") 
    img = models.ImageField(upload_to="rent/land/")
    
    def __str__(self):
        return " "







##### عمارة
class BuildingRent(models.Model):
    number = models.CharField(max_length=20, verbose_name="رقم الإعلان", null=True, blank=True)  
    position = GeopositionField() 
    title = models.CharField(max_length=200, verbose_name="عنوان الإعلان", null=True, blank=True) 

    interface = models.CharField(max_length=100, verbose_name="الواجهة", choices=INTERFACE_CHOICES, null=True, blank=True)
    sotres_count = models.IntegerField(default=0, verbose_name="عدد المحلات")
    apartments_count = models.IntegerField(default=0, verbose_name="عدد الشقق")
    property_age = models.IntegerField(default=0, verbose_name="عمر العقار") 

    # rooms = models.IntegerField(default=0, verbose_name="الغرف") 
    purpose = models.ForeignKey(Purpose, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="الغرض") 

    description = models.TextField(verbose_name="وصف العقار", default="   ")



    furnished = models.BooleanField(default=False, verbose_name="مؤثثة") 
    basement = models.BooleanField(default=False, verbose_name="قبو")
    water_exist = models.BooleanField(default=False, verbose_name="توفر الماء")
    power_exist = models.BooleanField(default=False, verbose_name="توفر الكهرباء")
    sanitation_exist = models.BooleanField(default=False, verbose_name="توفر الصرف")
    video = models.FileField(upload_to='rent/building/video', verbose_name="فيديو", null=True, blank=True)


    def save(self, *args, **kwargs): 
        if not self.number: 
            self.number = generate()
        super(BuildingRent, self).save(*args, **kwargs)



    def __str__(self):
        return str(self.number) 

    class Meta:
        verbose_name = 'BuildingRent'
        verbose_name_plural = 'BuildingRents'

class BuildingRentImage(models.Model):
    ad = models.ForeignKey(BuildingRent, on_delete=models.CASCADE, verbose_name="الإعلان") 
    img = models.ImageField(upload_to="rent/building/")
    
    def __str__(self):
        return " "




### مستودع
class WarehouseRent(models.Model):
    number = models.CharField(max_length=20, verbose_name="رقم الإعلان", null=True, blank=True)  
    position = GeopositionField() 
    title = models.CharField(max_length=200, verbose_name="عنوان الإعلان", null=True, blank=True) 
 
    interface = models.CharField(max_length=100, verbose_name="الواجهة", choices=INTERFACE_CHOICES, null=True, blank=True)
    street_width = models.FloatField(verbose_name="عرض الشارع", null=True, blank=True) 
    property_age = models.IntegerField(default=0, verbose_name="عمر العقار") 
    description = models.TextField(verbose_name="وصف العقار", default="   ")


    water_exist = models.BooleanField(default=False, verbose_name="توفر الماء")
    power_exist = models.BooleanField(default=False, verbose_name="توفر الكهرباء")
    sanitation_exist = models.BooleanField(default=False, verbose_name="توفر الصرف")

    
    video = models.FileField(upload_to='rent/warehouse/video', verbose_name="فيديو",null=True, blank=True)


    def save(self, *args, **kwargs): 
        if not self.number: 
            self.number = generate()
        super(WarehouseRent, self).save(*args, **kwargs)




class WarehouseRentImage(models.Model):
    ad = models.ForeignKey(WarehouseRent, on_delete=models.CASCADE, verbose_name="الإعلان") 
    img = models.ImageField(upload_to="rent/warehouse/")
    
    def __str__(self):
        return " "





## شقة مفروشة

class FurnishedApartmentRent(models.Model):
    number = models.CharField(max_length=20, verbose_name="رقم الإعلان", null=True, blank=True)  
    position = GeopositionField() 
    title = models.CharField(max_length=200, verbose_name="عنوان الإعلان", null=True, blank=True) 
    

    street_width = models.FloatField(verbose_name="عرض الشارع", null=True, blank=True) 

    rooms = models.IntegerField(default=0, verbose_name="الغرف") 

    lounges = models.IntegerField(default=0, verbose_name="الصالات")

    floor = models.IntegerField(default=0, verbose_name="الدور")    

    property_age = models.IntegerField(default=0, verbose_name="عمر العقار")    

    families = models.BooleanField(default=True, verbose_name="عوائل ام عزاب") 


    description = models.TextField(verbose_name="وصف العقار", default="   ")


    video = models.FileField(upload_to='rent/furnished-apartment/video', verbose_name="فيديو",null=True, blank=True)

    extenstion = models.BooleanField(default=False, verbose_name="ملحق")

    car_entrance= models.BooleanField(default=False, verbose_name="مدخل سيارة")

    ac = models.BooleanField(default=False, verbose_name="مكيف")


    water_exist = models.BooleanField(default=False, verbose_name="توفر الماء")
    power_exist = models.BooleanField(default=False, verbose_name="توفر الكهرباء")
    sanitation_exist = models.BooleanField(default=False, verbose_name="توفر الصرف")

    def save(self, *args, **kwargs): 
        if not self.number: 
            self.number = generate()
        super(FurnishedApartmentRent, self).save(*args, **kwargs)




class FurnishedApartmentRentImage(models.Model):
    ad = models.ForeignKey(FurnishedApartmentRent, on_delete=models.CASCADE, verbose_name="الإعلان") 
    img = models.ImageField(upload_to="rent/furnished-apartment/")
    
    def __str__(self):
        return " "





### شاليه

class ChaletRent(models.Model):
    number = models.CharField(max_length=20, verbose_name="رقم الإعلان", null=True, blank=True)  
    position = GeopositionField() 
    title = models.CharField(max_length=200, verbose_name="عنوان الإعلان", null=True, blank=True) 

    street_width = models.FloatField(verbose_name="عرض الشارع", null=True, blank=True) 

    property_age = models.IntegerField(default=0, verbose_name="عمر العقار")    

    lounges = models.IntegerField(default=0, verbose_name="الصالات")
    rooms = models.IntegerField(default=0, verbose_name="الغرف") 

    bathroom = models.IntegerField(default=0, verbose_name="عدد دورات المياه") 


    description = models.TextField(verbose_name="وصف العقار", default="   ")
    football_field = models.BooleanField(default=False, verbose_name="ملعب كرة قدم")
    volly_field = models.BooleanField(default=False, verbose_name="ملعب كرة طائرة")

    hair_tent_house = models.BooleanField(default=False, verbose_name="بيت شعر")

    kitchen = models.BooleanField(default=False, verbose_name="مطبخ")
    amusement = models.BooleanField(default=False, verbose_name="ملاهي")
    family_part = models.BooleanField(default=False, verbose_name="قسم عوائل")

    
    water_exist = models.BooleanField(default=False, verbose_name="توفر الماء")
    power_exist = models.BooleanField(default=False, verbose_name="توفر الكهرباء")
    sanitation_exist = models.BooleanField(default=False, verbose_name="توفر الصرف")


    video = models.FileField(upload_to='rent/chalet/video', verbose_name="فيديو",null=True, blank=True)


    def save(self, *args, **kwargs): 
        if not self.number: 
            self.number = generate()
        super(ChaletRent, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'ChaletRent'
        verbose_name_plural = 'ChaletRents'


class ChaletRentImage(models.Model):
    ad = models.ForeignKey(ChaletRent, on_delete=models.CASCADE, verbose_name="الإعلان") 
    img = models.ImageField(upload_to="rent/chalet/")
    
    def __str__(self):
        return " "



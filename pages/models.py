from django.db import models

# Create your models here.
class Home(models.Model): 
    date_created = models.DateTimeField(auto_now_add=True) 
    heading = models.CharField(max_length=255) 
    sub_heading = models.TextField() 

    def __str__(self):
        return str(self.date_created) 
    

    class Meta: 
        verbose_name = 'نص الصفحة الرئيسية' 
        verbose_name_plural = 'الصفحة الرئيسية'

class About(models.Model): 
    title = models.CharField(max_length=200, verbose_name="العنوان الرئيسي")
    description = models.TextField(verbose_name="الوصف")

    def __str__(self): 
        return self.title 
    


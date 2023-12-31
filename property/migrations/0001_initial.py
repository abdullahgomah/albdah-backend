# Generated by Django 4.2.5 on 2023-10-06 19:29

from django.db import migrations, models
import django.db.models.deletion
import geoposition.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApartmentRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=20, null=True, verbose_name='رقم الإعلان')),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='عنوان الإعلان')),
                ('price', models.IntegerField(default=0, verbose_name='السعر (ريال سعودي)')),
                ('space', models.IntegerField(default=0, verbose_name='المساحة (متر مربع)')),
                ('width', models.FloatField(verbose_name='العرض (متر)')),
                ('length', models.FloatField(verbose_name='الطول (متر)')),
                ('advertiser_relation', models.CharField(max_length=50, verbose_name='علاقة المعلن بالعقار')),
                ('exclusive', models.BooleanField(default=False, verbose_name='حصري')),
                ('video', models.FileField(upload_to='rent/apartment/video', verbose_name='فيديو')),
                ('street_width', models.FloatField(verbose_name='عرض الشارع')),
                ('rooms', models.IntegerField(default=0, verbose_name='الغرف')),
                ('lounges', models.IntegerField(default=0, verbose_name='الصالات')),
                ('bathroom', models.IntegerField(default=0, verbose_name='عدد دورات المياه')),
                ('floor', models.IntegerField(default=0, verbose_name='الدور')),
                ('property_age', models.IntegerField(default=0, verbose_name='عمر العقار')),
                ('families', models.BooleanField(default=True, verbose_name='عوائل ام عزاب')),
                ('rent_type', models.CharField(choices=[('yearly', 'سنوي'), ('monthly', 'شهري')], max_length=50, verbose_name='نوع الإيجار')),
                ('description', models.TextField(default='   ', verbose_name='وصف العقار')),
                ('furnished', models.BooleanField(default=False, verbose_name='مؤثثة')),
                ('kitchen', models.BooleanField(default=False, verbose_name='مطبخ')),
                ('extenstion', models.BooleanField(default=False, verbose_name='ملحق')),
                ('car_entrance', models.BooleanField(default=False, verbose_name='مدخل سيارة')),
                ('elevator', models.BooleanField(default=False, verbose_name='مصعد كهربائي')),
                ('ac', models.BooleanField(default=False, verbose_name='مكيف')),
                ('water_exist', models.BooleanField(default=False, verbose_name='توفر الماء')),
                ('power_exist', models.BooleanField(default=False, verbose_name='توفر الكهرباء')),
                ('sanitation_exist', models.BooleanField(default=False, verbose_name='توفر الصرف')),
                ('private_surface', models.BooleanField(default=False, verbose_name='سطح خاص')),
                ('in_villa', models.BooleanField(default=False, verbose_name='في فيلا')),
                ('two_enternace', models.BooleanField(default=False, verbose_name='مدخلين')),
                ('private_enternace', models.BooleanField(default=False, verbose_name='مدخل خاص')),
            ],
        ),
        migrations.CreateModel(
            name='BuildingRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=20, null=True, verbose_name='رقم الإعلان')),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='عنوان الإعلان')),
                ('interface', models.CharField(blank=True, choices=[('شمالية', 'شمالية'), ('جنوبية', 'جنوبية'), ('غربية', 'غربية'), ('شرقية', 'شرقية'), ('شمالية شرقية', 'شمالية شرقية'), ('شمالية غربية', 'شمالية غربية'), ('جنوبية شرقية', 'جنوبية شرقية'), ('جنوبية غربية', 'جنوبية غربية')], max_length=100, null=True, verbose_name='الواجهة')),
                ('sotres_count', models.IntegerField(default=0, verbose_name='عدد المحلات')),
                ('apartments_count', models.IntegerField(default=0, verbose_name='عدد الشقق')),
                ('property_age', models.IntegerField(default=0, verbose_name='عمر العقار')),
                ('description', models.TextField(default='   ', verbose_name='وصف العقار')),
                ('furnished', models.BooleanField(default=False, verbose_name='مؤثثة')),
                ('basement', models.BooleanField(default=False, verbose_name='قبو')),
                ('water_exist', models.BooleanField(default=False, verbose_name='توفر الماء')),
                ('power_exist', models.BooleanField(default=False, verbose_name='توفر الكهرباء')),
                ('sanitation_exist', models.BooleanField(default=False, verbose_name='توفر الصرف')),
                ('video', models.FileField(blank=True, null=True, upload_to='rent/building/video', verbose_name='فيديو')),
            ],
            options={
                'verbose_name': 'BuildingRent',
                'verbose_name_plural': 'BuildingRents',
            },
        ),
        migrations.CreateModel(
            name='ChaletRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=20, null=True, verbose_name='رقم الإعلان')),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='عنوان الإعلان')),
                ('street_width', models.FloatField(blank=True, null=True, verbose_name='عرض الشارع')),
                ('property_age', models.IntegerField(default=0, verbose_name='عمر العقار')),
                ('lounges', models.IntegerField(default=0, verbose_name='الصالات')),
                ('rooms', models.IntegerField(default=0, verbose_name='الغرف')),
                ('bathroom', models.IntegerField(default=0, verbose_name='عدد دورات المياه')),
                ('description', models.TextField(default='   ', verbose_name='وصف العقار')),
                ('football_field', models.BooleanField(default=False, verbose_name='ملعب كرة قدم')),
                ('volly_field', models.BooleanField(default=False, verbose_name='ملعب كرة طائرة')),
                ('hair_tent_house', models.BooleanField(default=False, verbose_name='بيت شعر')),
                ('kitchen', models.BooleanField(default=False, verbose_name='مطبخ')),
                ('amusement', models.BooleanField(default=False, verbose_name='ملاهي')),
                ('family_part', models.BooleanField(default=False, verbose_name='قسم عوائل')),
                ('water_exist', models.BooleanField(default=False, verbose_name='توفر الماء')),
                ('power_exist', models.BooleanField(default=False, verbose_name='توفر الكهرباء')),
                ('sanitation_exist', models.BooleanField(default=False, verbose_name='توفر الصرف')),
                ('video', models.FileField(blank=True, null=True, upload_to='rent/chalet/video', verbose_name='فيديو')),
            ],
            options={
                'verbose_name': 'ChaletRent',
                'verbose_name_plural': 'ChaletRents',
            },
        ),
        migrations.CreateModel(
            name='CommercialOfficeRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=20, null=True, verbose_name='رقم الإعلان')),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='عنوان الإعلان')),
                ('street_width', models.IntegerField(default=0, verbose_name='عرض الشارع')),
                ('floor', models.IntegerField(default=False, verbose_name='الدور')),
                ('rooms', models.IntegerField(default=0, verbose_name='الغرف')),
                ('lounges', models.IntegerField(default=0, verbose_name='الصالات')),
                ('bathroom', models.IntegerField(default=0, verbose_name='عدد دورات المياه')),
                ('property_age', models.IntegerField(default=0, verbose_name='عمر العقار')),
                ('description', models.TextField(blank=True, null=True, verbose_name='وصف العقار')),
                ('furnished', models.BooleanField(default=False, verbose_name='مؤثثة')),
                ('water_exist', models.BooleanField(default=False, verbose_name='توفر الماء')),
                ('power_exist', models.BooleanField(default=False, verbose_name='توفر الكهرباء')),
                ('sanitation_exist', models.BooleanField(default=False, verbose_name='توفر الصرف')),
                ('video', models.FileField(blank=True, null=True, upload_to='rent/commercial_office/video', verbose_name='فيديو')),
            ],
            options={
                'verbose_name': 'CommercialOfficeRent',
                'verbose_name_plural': 'CommercialOfficeRents',
            },
        ),
        migrations.CreateModel(
            name='FloorRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=20, null=True, verbose_name='رقم الإعلان')),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='عنوان الإعلان')),
                ('price', models.IntegerField(default=0, verbose_name='السعر (ريال سعودي)')),
                ('space', models.IntegerField(default=0, verbose_name='المساحة (متر مربع)')),
                ('width', models.FloatField(verbose_name='العرض (متر)')),
                ('length', models.FloatField(verbose_name='الطول (متر)')),
                ('advertiser_relation', models.CharField(max_length=50, verbose_name='علاقة المعلن بالعقار')),
                ('exclusive', models.BooleanField(default=False, verbose_name='حصري')),
                ('video', models.FileField(upload_to='rent/floor/video', verbose_name='فيديو')),
                ('street_width', models.FloatField(verbose_name='عرض الشارع')),
                ('rooms', models.IntegerField(default=0)),
                ('lounges', models.IntegerField(default=0, verbose_name='الصالات')),
                ('bathroom', models.IntegerField(default=0, verbose_name='عدد دورات المياه')),
                ('floor', models.IntegerField(default=0, verbose_name='الدور')),
                ('property_age', models.IntegerField(default=0, verbose_name='عمر العقار')),
                ('families', models.BooleanField(default=True, verbose_name='عوائل ام عزاب')),
                ('rent_type', models.CharField(choices=[('yearly', 'سنوي'), ('monthly', 'شهري')], max_length=50, verbose_name='نوع الإيجار')),
                ('description', models.TextField(verbose_name='وصف العقار')),
                ('furnished', models.BooleanField(default=False, verbose_name='مؤثثة')),
                ('kitchen', models.BooleanField(default=False, verbose_name='مطبخ')),
                ('extenstion', models.BooleanField(default=False, verbose_name='ملحق')),
                ('car_entrance', models.BooleanField(default=False, verbose_name='مدخل سيارة')),
                ('elevator', models.BooleanField(default=False, verbose_name='مصعد كهربائي')),
                ('ac', models.BooleanField(default=False, verbose_name='مكيف')),
                ('water_exist', models.BooleanField(default=False, verbose_name='توفر الماء')),
                ('power_exist', models.BooleanField(default=False, verbose_name='توفر الكهرباء')),
                ('sanitation_exist', models.BooleanField(default=False, verbose_name='توفر الصرف')),
                ('private_surface', models.BooleanField(default=False, verbose_name='سطح خاص')),
                ('in_villa', models.BooleanField(default=False, verbose_name='في فيلا')),
                ('two_enternace', models.BooleanField(default=False, verbose_name='مدخلين')),
                ('private_enternace', models.BooleanField(default=False, verbose_name='مدخل خاص')),
            ],
            options={
                'verbose_name': 'FloorRent',
                'verbose_name_plural': 'FloorRents',
            },
        ),
        migrations.CreateModel(
            name='FurnishedApartmentRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=20, null=True, verbose_name='رقم الإعلان')),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='عنوان الإعلان')),
                ('street_width', models.FloatField(blank=True, null=True, verbose_name='عرض الشارع')),
                ('rooms', models.IntegerField(default=0, verbose_name='الغرف')),
                ('lounges', models.IntegerField(default=0, verbose_name='الصالات')),
                ('floor', models.IntegerField(default=0, verbose_name='الدور')),
                ('property_age', models.IntegerField(default=0, verbose_name='عمر العقار')),
                ('families', models.BooleanField(default=True, verbose_name='عوائل ام عزاب')),
                ('description', models.TextField(default='   ', verbose_name='وصف العقار')),
                ('video', models.FileField(blank=True, null=True, upload_to='rent/furnished-apartment/video', verbose_name='فيديو')),
                ('extenstion', models.BooleanField(default=False, verbose_name='ملحق')),
                ('car_entrance', models.BooleanField(default=False, verbose_name='مدخل سيارة')),
                ('ac', models.BooleanField(default=False, verbose_name='مكيف')),
                ('water_exist', models.BooleanField(default=False, verbose_name='توفر الماء')),
                ('power_exist', models.BooleanField(default=False, verbose_name='توفر الكهرباء')),
                ('sanitation_exist', models.BooleanField(default=False, verbose_name='توفر الصرف')),
            ],
        ),
        migrations.CreateModel(
            name='LandRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=20, null=True, verbose_name='رقم الإعلان')),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='عنوان الإعلان')),
                ('interface', models.CharField(blank=True, choices=[('شمالية', 'شمالية'), ('جنوبية', 'جنوبية'), ('غربية', 'غربية'), ('شرقية', 'شرقية'), ('شمالية شرقية', 'شمالية شرقية'), ('شمالية غربية', 'شمالية غربية'), ('جنوبية شرقية', 'جنوبية شرقية'), ('جنوبية غربية', 'جنوبية غربية')], max_length=100, null=True, verbose_name='الواجهة')),
                ('street_width', models.FloatField(blank=True, null=True, verbose_name='عرض الشارع')),
                ('description', models.TextField(default='  ', verbose_name='وصف العقار')),
                ('water_exist', models.BooleanField(default=False, verbose_name='توفر الماء')),
                ('power_exist', models.BooleanField(default=False, verbose_name='توفر الكهرباء')),
                ('sanitation_exist', models.BooleanField(default=False, verbose_name='توفر الصرف')),
                ('video', models.FileField(blank=True, null=True, upload_to='rent/land/video', verbose_name='فيديو')),
            ],
            options={
                'verbose_name': 'LandRent',
                'verbose_name_plural': 'LandRents',
            },
        ),
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='الاسم')),
            ],
        ),
        migrations.CreateModel(
            name='RestHouseRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=20, null=True, verbose_name='رقم الإعلان')),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='عنوان الإعلان')),
                ('street_width', models.IntegerField(default=0, verbose_name='عرض الشارع')),
                ('property_age', models.IntegerField(default=0, verbose_name='عمر العقار')),
                ('lounges', models.IntegerField(default=0, verbose_name='الصالات')),
                ('rooms', models.IntegerField(default=0, verbose_name='الغرف')),
                ('bathroom', models.IntegerField(default=0, verbose_name='عدد دورات المياه')),
                ('description', models.TextField(blank=True, null=True, verbose_name='وصف العقار')),
                ('pool', models.BooleanField(default=False, verbose_name='مسبح')),
                ('football_field', models.BooleanField(default=False, verbose_name='ملعب كرة قدم')),
                ('volly_field', models.BooleanField(default=False, verbose_name='ملعب كرة طائرة')),
                ('hair_tent_house', models.BooleanField(default=False, verbose_name='بيت شعر')),
                ('kitchen', models.BooleanField(default=False, verbose_name='مطبخ')),
                ('amusement', models.BooleanField(default=False, verbose_name='ملاهي')),
                ('family_part', models.BooleanField(default=False, verbose_name='قسم عوائل')),
                ('water_exist', models.BooleanField(default=False, verbose_name='توفر الماء')),
                ('power_exist', models.BooleanField(default=False, verbose_name='توفر الكهرباء')),
                ('sanitation_exist', models.BooleanField(default=False, verbose_name='توفر الصرف')),
                ('video', models.FileField(blank=True, null=True, upload_to='rent/rest_house/video', verbose_name='فيديو')),
            ],
            options={
                'verbose_name': 'RestHouseRent',
                'verbose_name_plural': 'RestHouseRents',
            },
        ),
        migrations.CreateModel(
            name='ShopRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=20, null=True, verbose_name='رقم الإعلان')),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='عنوان الإعلان')),
                ('interface', models.CharField(blank=True, choices=[('شمالية', 'شمالية'), ('جنوبية', 'جنوبية'), ('غربية', 'غربية'), ('شرقية', 'شرقية'), ('شمالية شرقية', 'شمالية شرقية'), ('شمالية غربية', 'شمالية غربية'), ('جنوبية شرقية', 'جنوبية شرقية'), ('جنوبية غربية', 'جنوبية غربية')], max_length=100, null=True, verbose_name='الواجهة')),
                ('street_width', models.IntegerField(default=0, verbose_name='عرض الشارع')),
                ('property_age', models.IntegerField(default=0, verbose_name='عمر العقار')),
                ('description', models.TextField(blank=True, null=True, verbose_name='وصف العقار')),
                ('water_exist', models.BooleanField(default=False, verbose_name='توفر الماء')),
                ('power_exist', models.BooleanField(default=False, verbose_name='توفر الكهرباء')),
                ('sanitation_exist', models.BooleanField(default=False, verbose_name='توفر الصرف')),
                ('video', models.FileField(blank=True, null=True, upload_to='rent/shop_rent/', verbose_name='فيديو')),
            ],
            options={
                'verbose_name': 'ShopRent',
                'verbose_name_plural': 'ShopRents',
            },
        ),
        migrations.CreateModel(
            name='VillaRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=20, null=True, verbose_name='رقم الإعلان')),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='عنوان الإعلان')),
                ('interface', models.CharField(choices=[('شمالية', 'شمالية'), ('جنوبية', 'جنوبية'), ('غربية', 'غربية'), ('شرقية', 'شرقية'), ('شمالية شرقية', 'شمالية شرقية'), ('شمالية غربية', 'شمالية غربية'), ('جنوبية شرقية', 'جنوبية شرقية'), ('جنوبية غربية', 'جنوبية غربية')], max_length=100, verbose_name='الواجهة')),
                ('price', models.IntegerField(default=0, verbose_name='السعر (ريال سعودي)')),
                ('space', models.IntegerField(default=0, verbose_name='المساحة (متر مربع)')),
                ('width', models.FloatField(verbose_name='العرض (متر)')),
                ('length', models.FloatField(verbose_name='الطول (متر)')),
                ('advertiser_relation', models.CharField(max_length=50, verbose_name='علاقة المعلن بالعقار')),
                ('exclusive', models.BooleanField(default=False, verbose_name='حصري')),
                ('video', models.FileField(upload_to='rent/villa/video', verbose_name='فيديو')),
                ('street_width', models.FloatField(verbose_name='عرض الشارع')),
                ('rooms', models.IntegerField(default=0)),
                ('lounges', models.IntegerField(default=0, verbose_name='الصالات')),
                ('bathroom', models.IntegerField(default=0, verbose_name='عدد دورات المياه')),
                ('floor', models.IntegerField(default=0, verbose_name='الدور')),
                ('property_age', models.IntegerField(default=0, verbose_name='عمر العقار')),
                ('families', models.BooleanField(default=True, verbose_name='عوائل ام عزاب')),
                ('rent_type', models.CharField(choices=[('yearly', 'سنوي'), ('monthly', 'شهري')], max_length=50, verbose_name='نوع الإيجار')),
                ('description', models.TextField(verbose_name='وصف العقار')),
                ('furnished', models.BooleanField(default=False, verbose_name='مؤثثة')),
                ('kitchen', models.BooleanField(default=False, verbose_name='مطبخ')),
                ('extenstion', models.BooleanField(default=False, verbose_name='ملحق')),
                ('car_entrance', models.BooleanField(default=False, verbose_name='مدخل سيارة')),
                ('elevator', models.BooleanField(default=False, verbose_name='مصعد كهربائي')),
                ('ac', models.BooleanField(default=False, verbose_name='مكيف')),
                ('water_exist', models.BooleanField(default=False, verbose_name='توفر الماء')),
                ('power_exist', models.BooleanField(default=False, verbose_name='توفر الكهرباء')),
                ('sanitation_exist', models.BooleanField(default=False, verbose_name='توفر الصرف')),
                ('private_surface', models.BooleanField(default=False, verbose_name='سطح خاص')),
                ('in_villa', models.BooleanField(default=False, verbose_name='في فيلا')),
                ('two_enternace', models.BooleanField(default=False, verbose_name='مدخلين')),
                ('private_enternace', models.BooleanField(default=False, verbose_name='مدخل خاص')),
                ('driver_room', models.BooleanField(default=False, verbose_name='غرفة سائق')),
                ('maid_room', models.BooleanField(default=False, verbose_name='غرفة خادمة')),
                ('duplex', models.BooleanField(default=False, verbose_name='دوبلكس')),
                ('basement', models.BooleanField(default=False, verbose_name='قبو')),
                ('yard', models.BooleanField(default=False, verbose_name='حوش')),
                ('hair_tent_house', models.BooleanField(default=False, verbose_name='بيت شعر')),
            ],
            options={
                'verbose_name': 'VillaRent',
                'verbose_name_plural': 'VillaRents',
            },
        ),
        migrations.CreateModel(
            name='WarehouseRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=20, null=True, verbose_name='رقم الإعلان')),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='عنوان الإعلان')),
                ('interface', models.CharField(blank=True, choices=[('شمالية', 'شمالية'), ('جنوبية', 'جنوبية'), ('غربية', 'غربية'), ('شرقية', 'شرقية'), ('شمالية شرقية', 'شمالية شرقية'), ('شمالية غربية', 'شمالية غربية'), ('جنوبية شرقية', 'جنوبية شرقية'), ('جنوبية غربية', 'جنوبية غربية')], max_length=100, null=True, verbose_name='الواجهة')),
                ('street_width', models.FloatField(blank=True, null=True, verbose_name='عرض الشارع')),
                ('property_age', models.IntegerField(default=0, verbose_name='عمر العقار')),
                ('description', models.TextField(default='   ', verbose_name='وصف العقار')),
                ('water_exist', models.BooleanField(default=False, verbose_name='توفر الماء')),
                ('power_exist', models.BooleanField(default=False, verbose_name='توفر الكهرباء')),
                ('sanitation_exist', models.BooleanField(default=False, verbose_name='توفر الصرف')),
                ('video', models.FileField(blank=True, null=True, upload_to='rent/warehouse/video', verbose_name='فيديو')),
            ],
        ),
        migrations.CreateModel(
            name='WarehouseRentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='rent/warehouse/')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.warehouserent', verbose_name='الإعلان')),
            ],
        ),
        migrations.CreateModel(
            name='VillaRentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='rent/villa/')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.villarent', verbose_name='الإعلان')),
            ],
        ),
        migrations.CreateModel(
            name='ShopRentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='rent/shop_rent/')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.shoprent', verbose_name='الإعلان')),
            ],
        ),
        migrations.CreateModel(
            name='RestHouseRentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='rent/rest_house/')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.resthouserent', verbose_name='الإعلان')),
            ],
        ),
        migrations.CreateModel(
            name='LandRentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='rent/land/')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.landrent', verbose_name='الإعلان')),
            ],
        ),
        migrations.AddField(
            model_name='landrent',
            name='purpose',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.purpose'),
        ),
        migrations.CreateModel(
            name='FurnishedApartmentRentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='rent/furnished-apartment/')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.furnishedapartmentrent', verbose_name='الإعلان')),
            ],
        ),
        migrations.CreateModel(
            name='FloorRentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='rent/floor/')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.floorrent', verbose_name='الإعلان')),
            ],
        ),
        migrations.CreateModel(
            name='CommercialOfficeRentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='rent/commercial_office/')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.commercialofficerent', verbose_name='الإعلان')),
            ],
        ),
        migrations.CreateModel(
            name='ChaletRentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='rent/chalet/')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.chaletrent', verbose_name='الإعلان')),
            ],
        ),
        migrations.CreateModel(
            name='BuildingRentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='rent/building/')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.buildingrent', verbose_name='الإعلان')),
            ],
        ),
        migrations.AddField(
            model_name='buildingrent',
            name='purpose',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.purpose', verbose_name='الغرض'),
        ),
        migrations.CreateModel(
            name='ApartmentRentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='rent/apartment/')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imgs', to='property.apartmentrent', verbose_name='الإعلان')),
            ],
        ),
    ]

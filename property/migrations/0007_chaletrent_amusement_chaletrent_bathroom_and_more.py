# Generated by Django 4.2.5 on 2023-09-28 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_warehouserent_description_warehouserent_interface_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaletrent',
            name='amusement',
            field=models.BooleanField(default=False, verbose_name='ملاهي'),
        ),
        migrations.AddField(
            model_name='chaletrent',
            name='bathroom',
            field=models.IntegerField(default=0, verbose_name='عدد دورات المياه'),
        ),
        migrations.AddField(
            model_name='chaletrent',
            name='description',
            field=models.TextField(default='   ', verbose_name='وصف العقار'),
        ),
        migrations.AddField(
            model_name='chaletrent',
            name='family_part',
            field=models.BooleanField(default=False, verbose_name='قسم عوائل'),
        ),
        migrations.AddField(
            model_name='chaletrent',
            name='football_field',
            field=models.BooleanField(default=False, verbose_name='ملعب كرة قدم'),
        ),
        migrations.AddField(
            model_name='chaletrent',
            name='hair_tent_house',
            field=models.BooleanField(default=False, verbose_name='بيت شعر'),
        ),
        migrations.AddField(
            model_name='chaletrent',
            name='kitchen',
            field=models.BooleanField(default=False, verbose_name='مطبخ'),
        ),
        migrations.AddField(
            model_name='chaletrent',
            name='lounges',
            field=models.IntegerField(default=0, verbose_name='الصالات'),
        ),
        migrations.AddField(
            model_name='chaletrent',
            name='power_exist',
            field=models.BooleanField(default=False, verbose_name='توفر الكهرباء'),
        ),
        migrations.AddField(
            model_name='chaletrent',
            name='property_age',
            field=models.IntegerField(default=0, verbose_name='عمر العقار'),
        ),
        migrations.AddField(
            model_name='chaletrent',
            name='rooms',
            field=models.IntegerField(default=0, verbose_name='الغرف'),
        ),
        migrations.AddField(
            model_name='chaletrent',
            name='sanitation_exist',
            field=models.BooleanField(default=False, verbose_name='توفر الصرف'),
        ),
        migrations.AddField(
            model_name='chaletrent',
            name='street_width',
            field=models.FloatField(blank=True, null=True, verbose_name='عرض الشارع'),
        ),
        migrations.AddField(
            model_name='chaletrent',
            name='volly_field',
            field=models.BooleanField(default=False, verbose_name='ملعب كرة طائرة'),
        ),
        migrations.AddField(
            model_name='chaletrent',
            name='water_exist',
            field=models.BooleanField(default=False, verbose_name='توفر الماء'),
        ),
        migrations.AddField(
            model_name='furnishedapartmentrent',
            name='ac',
            field=models.BooleanField(default=False, verbose_name='مكيف'),
        ),
        migrations.AddField(
            model_name='furnishedapartmentrent',
            name='car_entrance',
            field=models.BooleanField(default=False, verbose_name='مدخل سيارة'),
        ),
        migrations.AddField(
            model_name='furnishedapartmentrent',
            name='description',
            field=models.TextField(default='   ', verbose_name='وصف العقار'),
        ),
        migrations.AddField(
            model_name='furnishedapartmentrent',
            name='extenstion',
            field=models.BooleanField(default=False, verbose_name='ملحق'),
        ),
        migrations.AddField(
            model_name='furnishedapartmentrent',
            name='families',
            field=models.BooleanField(default=True, verbose_name='عوائل ام عزاب'),
        ),
        migrations.AddField(
            model_name='furnishedapartmentrent',
            name='floor',
            field=models.IntegerField(default=0, verbose_name='الدور'),
        ),
        migrations.AddField(
            model_name='furnishedapartmentrent',
            name='lounges',
            field=models.IntegerField(default=0, verbose_name='الصالات'),
        ),
        migrations.AddField(
            model_name='furnishedapartmentrent',
            name='power_exist',
            field=models.BooleanField(default=False, verbose_name='توفر الكهرباء'),
        ),
        migrations.AddField(
            model_name='furnishedapartmentrent',
            name='property_age',
            field=models.IntegerField(default=0, verbose_name='عمر العقار'),
        ),
        migrations.AddField(
            model_name='furnishedapartmentrent',
            name='rooms',
            field=models.IntegerField(default=0, verbose_name='الغرف'),
        ),
        migrations.AddField(
            model_name='furnishedapartmentrent',
            name='sanitation_exist',
            field=models.BooleanField(default=False, verbose_name='توفر الصرف'),
        ),
        migrations.AddField(
            model_name='furnishedapartmentrent',
            name='street_width',
            field=models.FloatField(blank=True, null=True, verbose_name='عرض الشارع'),
        ),
        migrations.AddField(
            model_name='furnishedapartmentrent',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='rent/furnished-apartment/video', verbose_name='فيديو'),
        ),
        migrations.AddField(
            model_name='furnishedapartmentrent',
            name='water_exist',
            field=models.BooleanField(default=False, verbose_name='توفر الماء'),
        ),
        migrations.AddField(
            model_name='warehouserent',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='rent/warehouse/video', verbose_name='فيديو'),
        ),
        migrations.AlterField(
            model_name='buildingrentimage',
            name='ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.buildingrent', verbose_name='الإعلان'),
        ),
        migrations.AlterField(
            model_name='commercialofficerentimage',
            name='ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.commercialofficerent', verbose_name='الإعلان'),
        ),
        migrations.AlterField(
            model_name='landrentimage',
            name='ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.landrent', verbose_name='الإعلان'),
        ),
        migrations.CreateModel(
            name='WarehouseRentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='rent/warehouse/')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.warehouserent', verbose_name='الإعلان')),
            ],
        ),
    ]

# Generated by Django 4.2.5 on 2023-10-24 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0031_apartmentrent_city_apartmentrent_neighborhood_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartmentrentimage',
            name='main',
            field=models.BooleanField(blank=True, default=0, null=True, verbose_name='صورة رئيسية'),
        ),
        migrations.AddField(
            model_name='buildingrentimage',
            name='main',
            field=models.BooleanField(blank=True, default=0, null=True, verbose_name='صورة رئيسية'),
        ),
        migrations.AddField(
            model_name='chaletrentimage',
            name='main',
            field=models.BooleanField(blank=True, default=0, null=True, verbose_name='صورة رئيسية'),
        ),
        migrations.AddField(
            model_name='commercialofficerentimage',
            name='main',
            field=models.BooleanField(blank=True, default=0, null=True, verbose_name='صورة رئيسية'),
        ),
        migrations.AddField(
            model_name='floorrentimage',
            name='main',
            field=models.BooleanField(blank=True, default=0, null=True, verbose_name='صورة رئيسية'),
        ),
        migrations.AddField(
            model_name='furnishedapartmentrentimage',
            name='main',
            field=models.BooleanField(blank=True, default=0, null=True, verbose_name='صورة رئيسية'),
        ),
        migrations.AddField(
            model_name='landrentimage',
            name='main',
            field=models.BooleanField(blank=True, default=0, null=True, verbose_name='صورة رئيسية'),
        ),
        migrations.AddField(
            model_name='resthouserentimage',
            name='main',
            field=models.BooleanField(blank=True, default=0, null=True, verbose_name='صورة رئيسية'),
        ),
        migrations.AddField(
            model_name='shoprentimage',
            name='main',
            field=models.BooleanField(blank=True, default=0, null=True, verbose_name='صورة رئيسية'),
        ),
        migrations.AddField(
            model_name='villarentimage',
            name='main',
            field=models.BooleanField(blank=True, default=0, null=True, verbose_name='صورة رئيسية'),
        ),
        migrations.AddField(
            model_name='warehouserentimage',
            name='main',
            field=models.BooleanField(blank=True, default=0, null=True, verbose_name='صورة رئيسية'),
        ),
    ]

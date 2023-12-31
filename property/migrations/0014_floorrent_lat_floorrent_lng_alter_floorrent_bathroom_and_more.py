# Generated by Django 4.2.5 on 2023-10-19 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_alter_apartmentrent_bathroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='floorrent',
            name='lat',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='floorrent',
            name='lng',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='floorrent',
            name='bathroom',
            field=models.CharField(blank=True, default=0, max_length=10, null=True, verbose_name='عدد دورات المياه'),
        ),
        migrations.AlterField(
            model_name='floorrent',
            name='floor',
            field=models.CharField(blank=True, default=0, max_length=10, null=True, verbose_name='الدور'),
        ),
        migrations.AlterField(
            model_name='floorrent',
            name='lounges',
            field=models.CharField(blank=True, default=0, max_length=10, null=True, verbose_name='الصالات'),
        ),
        migrations.AlterField(
            model_name='floorrent',
            name='property_age',
            field=models.CharField(blank=True, default=0, max_length=10, null=True, verbose_name='عمر العقار'),
        ),
        migrations.AlterField(
            model_name='floorrent',
            name='rooms',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
    ]

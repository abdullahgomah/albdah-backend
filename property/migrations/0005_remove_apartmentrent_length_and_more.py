# Generated by Django 4.2.5 on 2023-10-11 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_alter_apartmentrent_rent_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartmentrent',
            name='length',
        ),
        migrations.RemoveField(
            model_name='apartmentrent',
            name='width',
        ),
    ]

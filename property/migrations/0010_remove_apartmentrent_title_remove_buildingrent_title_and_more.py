# Generated by Django 4.2.5 on 2023-10-15 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_alter_apartmentrent_property_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartmentrent',
            name='title',
        ),
        migrations.RemoveField(
            model_name='buildingrent',
            name='title',
        ),
        migrations.RemoveField(
            model_name='chaletrent',
            name='title',
        ),
        migrations.RemoveField(
            model_name='commercialofficerent',
            name='title',
        ),
        migrations.RemoveField(
            model_name='floorrent',
            name='title',
        ),
        migrations.RemoveField(
            model_name='furnishedapartmentrent',
            name='title',
        ),
        migrations.RemoveField(
            model_name='landrent',
            name='title',
        ),
        migrations.RemoveField(
            model_name='resthouserent',
            name='title',
        ),
        migrations.RemoveField(
            model_name='shoprent',
            name='title',
        ),
        migrations.RemoveField(
            model_name='villarent',
            name='title',
        ),
        migrations.RemoveField(
            model_name='warehouserent',
            name='title',
        ),
    ]

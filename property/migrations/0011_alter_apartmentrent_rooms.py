# Generated by Django 4.2.5 on 2023-10-18 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_remove_apartmentrent_title_remove_buildingrent_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentrent',
            name='rooms',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='الغرف'),
        ),
    ]
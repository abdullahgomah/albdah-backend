# Generated by Django 4.2.5 on 2023-10-11 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_alter_apartmentrent_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentrent',
            name='street_width',
            field=models.FloatField(blank=True, null=True, verbose_name='عرض الشارع'),
        ),
    ]
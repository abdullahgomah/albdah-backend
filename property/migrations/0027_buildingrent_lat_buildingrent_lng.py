# Generated by Django 4.2.5 on 2023-10-20 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0026_alter_buildingrent_apartments_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildingrent',
            name='lat',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='buildingrent',
            name='lng',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
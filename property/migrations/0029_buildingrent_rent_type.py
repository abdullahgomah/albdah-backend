# Generated by Django 4.2.5 on 2023-10-20 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0028_buildingrent_advertiser_relation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildingrent',
            name='rent_type',
            field=models.CharField(blank=True, choices=[('yearly', 'سنوي'), ('monthly', 'شهري')], max_length=50, null=True, verbose_name='نوع الإيجار'),
        ),
    ]

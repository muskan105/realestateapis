# Generated by Django 3.2.18 on 2023-05-09 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimonial_data', '0003_auto_20230509_0920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ghar',
            name='price',
        ),
        migrations.AddField(
            model_name='ghar',
            name='bhk',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='ghar',
            name='place',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='ghar',
            name='price_amount',
            field=models.IntegerField(default=0, null=True),
        ),
    ]

# Generated by Django 3.2.18 on 2023-05-09 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matrimonial_data', '0002_auto_20230327_0636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ghar',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='ghar',
            name='longitude',
        ),
    ]

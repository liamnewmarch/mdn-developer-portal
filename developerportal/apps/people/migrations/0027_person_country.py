# Generated by Django 2.2.4 on 2019-09-25 10:39

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0026_auto_20190819_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='country',
            field=django_countries.fields.CountryField(blank=True, default='', max_length=2),
        ),
    ]
# Generated by Django 4.2.7 on 2024-04-11 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_country_abbreviation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='country_name_fr',
            field=models.CharField(max_length=200),
        ),
    ]

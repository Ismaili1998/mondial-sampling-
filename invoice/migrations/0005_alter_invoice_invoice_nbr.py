# Generated by Django 4.2.7 on 2023-12-02 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_remove_invoice_commercialoffer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_nbr',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-02 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0006_alter_invoice_client_nbr_alter_invoice_invoice_nbr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='client_nbr',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]

# Generated by Django 4.2.7 on 2024-05-12 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_client_client_name'),
        ('invoice', '0001_initial'),
    ]

    operations = [
        
        migrations.AddField(
            model_name='invoice',
            name='commission',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='confirmed',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='invoice',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.currency'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='delivery_time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='delivery_time_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.timeunit'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='destination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.destination'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AddField(
            model_name='invoice',
            name='duration_in_days',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='local_contact',
            field=models.BooleanField(default=1),
        ),
        migrations.AddField(
            model_name='invoice',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.payment'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='payment_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='project',
            field=models.ForeignKey(default=1000, on_delete=django.db.models.deletion.CASCADE, to='project.project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='rank',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='shipping',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.shipping'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='shipping_fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='invoice',
            name='transport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.transport'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='transport_fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='invoice',
            name='warranty_period',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

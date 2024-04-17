# Generated by Django 4.2.7 on 2024-04-11 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quoteRequest', '0001_initial'),
        ('project', '0004_alter_client_client_name'),
        ('commercialOffer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_nbr', models.CharField(max_length=30, unique=True)),
                ('description_fr', models.TextField(max_length=1500, null=True)),
                ('description_de', models.TextField(blank=True, max_length=1500, null=True)),
                ('description_en', models.TextField(blank=True, max_length=1500, null=True)),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('net_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('hs_code', models.CharField(blank=True, max_length=150, null=True)),
                ('customs_description', models.TextField(blank=True, max_length=500, null=True)),
                ('comment', models.TextField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'article',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ArticleUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'article_unit',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('quantity', models.DecimalField(decimal_places=2, default=1, max_digits=10)),
                ('margin', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.article')),
                ('commercialOffer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='commercialOffer.commercialoffer')),
                ('quoteRequest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quoteRequest.quoterequest')),
            ],
            options={
                'db_table': 'order',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='article_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.articleunit'),
        ),
        migrations.AddField(
            model_name='article',
            name='projects',
            field=models.ManyToManyField(to='project.project'),
        ),
    ]

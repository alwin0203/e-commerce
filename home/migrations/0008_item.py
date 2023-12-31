# Generated by Django 4.2.4 on 2023-08-22 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_collection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('item_price_offer', models.DecimalField(decimal_places=2, max_digits=5)),
                ('item_desc', models.TextField()),
                ('item_image', models.ImageField(null=True, upload_to='items')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('collection_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.collection')),
            ],
        ),
    ]

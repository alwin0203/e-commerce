# Generated by Django 4.2.4 on 2023-08-17 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clothing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image3', models.ImageField(upload_to='media/images')),
                ('product_name3', models.CharField(max_length=50)),
                ('product_price3', models.IntegerField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='manwomen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image1', models.ImageField(upload_to='media/images')),
                ('product_name1', models.CharField(max_length=50)),
                ('product_price1', models.IntegerField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='panttrouser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image2', models.ImageField(upload_to='media/images')),
                ('product_name2', models.CharField(max_length=50)),
                ('product_price2', models.IntegerField(max_length=50)),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-09 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='descption',
            field=models.TextField(default='Default description'),
        ),
    ]

# Generated by Django 4.0.1 on 2022-03-23 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_alter_shop_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='shop',
            name='image',
            field=models.ImageField(upload_to='uploads/images/Shop'),
        ),
    ]

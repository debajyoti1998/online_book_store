# Generated by Django 3.1.4 on 2021-01-02 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_product', '0007_remove_add_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_product',
            name='image',
            field=models.ImageField(default='abc', upload_to='pics/products/'),
            preserve_default=False,
        ),
    ]
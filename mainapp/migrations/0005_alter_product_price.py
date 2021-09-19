# Generated by Django 3.2.4 on 2021-09-14 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Price should Grater than 20', max_digits=8),
        ),
    ]

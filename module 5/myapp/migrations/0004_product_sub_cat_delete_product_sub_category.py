# Generated by Django 4.2.4 on 2023-09-13 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_product_sub_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_sub_cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30)),
                ('Product_price', models.CharField(max_length=50)),
                ('Product_model', models.CharField(max_length=50)),
                ('Product_ram', models.CharField(max_length=50)),
                ('Product_img', models.ImageField(default='', upload_to='image/')),
            ],
        ),
        migrations.DeleteModel(
            name='Product_sub_category',
        ),
    ]

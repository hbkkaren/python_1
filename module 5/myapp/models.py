from django.db import models


class User(models.Model):
    usertype = models.CharField(max_length=100,default='Admin')
    name = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobile=models.PositiveIntegerField()
    gender=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.email


class Product_mst(models.Model):
    id = models.CharField(max_length=100, primary_key=True),
    product_brand = models.CharField(max_length=100)


class Product_sub_cat(models.Model):
    pname=models.CharField(max_length=30)
    product_price= models.CharField(max_length=50)
    product_model= models.CharField(max_length=50)
    product_ram= models.CharField(max_length=50)
    product_img= models.ImageField(upload_to='image/',default="")


   


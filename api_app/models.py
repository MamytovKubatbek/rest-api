
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=20, verbose_name="Бренд")
    img = models.ImageField(upload_to="Brend_img")
    create_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-create_data', '-update_data']

        verbose_name_plural="Бренд"
        verbose_name = "Бренд"



class Products(models.Model):

    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("for kids", "for kids"),
    )

    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL,  verbose_name="Brand", null=True)
    title = models.CharField(max_length=50, verbose_name="Name product", null=True)
    description = models.TextField(verbose_name="description", null=True )
    size = models.IntegerField(default="38", verbose_name="Size", null=True)
    price = models.FloatField(default="0.00", verbose_name="Price", null=True)
    quant = models.IntegerField(default="5", verbose_name="quant", null=True)
    image = models.ImageField(upload_to="Product_img", verbose_name="image", null=True)
    gender = models.CharField( max_length=100, verbose_name="Gender", choices=GENDER, null=True)
    create_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['-create_data', '-update_data']
        verbose_name_plural="Продукты"
        verbose_name = "Продукты"


class Cart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL,  verbose_name="Product", null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL,  verbose_name="Brand", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.FloatField(default="0.00", verbose_name="Price", null=True)
    quant = models.IntegerField(default="5", verbose_name="quant", null=True)
    create_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.product)
     
    class Meta:
        ordering = ['-create_data', '-update_data']

        verbose_name_plural="Карзина"


class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL,  verbose_name="Product", null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL,  verbose_name="Brand", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.FloatField(default="0.00", verbose_name="Price")
    quant = models.IntegerField(default="5", verbose_name="quant")
    create_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.product)
    
    class Meta:
        ordering = ['-create_data', '-update_data']
        verbose_name_plural="Order"





class Favorite(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL,  verbose_name="Product", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.FloatField(default="0.00", verbose_name="Price")
    quant = models.IntegerField(default="5", verbose_name="quant")
    create_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.product)
    
    class Meta:
        ordering = ['-create_data', '-update_data']

        verbose_name_plural="Favorite"


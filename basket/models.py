from django.db import models

# Create your models here.
class Basket(models.Model):
    """base class for basket"""
    basket_id = models.AutoField(u'ID', primary_key=True)
    #TODO: add user FK to basket

class Product(models.Model):
    """base class for product"""
    product_id = models.AutoField(u'ID', primary_key=True)
    product_name = models.CharField(u'Название', max_length=250)
    product_description = models.TextField(u'Описание')
    product_price = models.IntegerField(u'Цена')
    product_photo = models.ImageField(u'Фото', upload_to="upload")
    basket_id = models.ForeignKey(Basket, u'Корзина', null=True, 
                                  default=None, on_delete=models.SET_NULL)

class Photo(models.Model):
    """base class for additional photos for product"""
    product = models.ForeignKey(Product, u'Товар', null=True,
                                default=None, on_delete=models.SET_NULL)
    photo = models.ImageField(u'Файл', upload_to="upload")


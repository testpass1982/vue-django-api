from django.db import models
from django.conf import settings

# Create your models here.
class Product(models.Model):
    """base class for product"""
    product_id = models.AutoField(u'ID', primary_key=True)
    product_name = models.CharField(u'Название', max_length=250)
    product_description = models.TextField(u'Описание')
    product_price = models.IntegerField(u'Цена')
    product_photo = models.ImageField(u'Фото', upload_to="upload")
    # basket_id = models.ForeignKey(Basket, null=True, blank=True,
    #                               default=None, on_delete=models.SET_NULL)

class Basket(models.Model):
    """base class for basket"""
    basket_id = models.AutoField(u'ID', primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(u'Количество товаров')
    # total_price = models.PositiveIntegerField(u'Стоимость всего')
    #TODO: add user FK to basket


class Photo(models.Model):
    """base class for additional photos for product"""
    product = models.ForeignKey(Product, null=True, blank=True,
                                default=None, on_delete=models.SET_NULL)
    photo = models.ImageField(u'Файл', upload_to="upload")


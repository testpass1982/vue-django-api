from django.contrib import admin
from .models import Basket, Photo, Product

# Register your models here.
admin.site.register(Basket)
admin.site.register(Photo)
admin.site.register(Product)
#TODO: make a preview for photos in admin interface
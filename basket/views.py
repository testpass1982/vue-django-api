from django.shortcuts import render
from .models import Product, Photo, Basket
# from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from django.views.generic import TemplateView
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework import generics

# Create your views here.

#main page view
# api decorator
# def index(request):
#     title = 'Index page'
#     content = {
#         'title': title
#     }
#     return render(request, 'basket/index.html', content)

# class ProductList(generics.RetrieveAPIView):
#     renderer_classes = (TemplateHTMLRenderer,)

#     def get(self, request, format=None):
#         """return a list of all products"""
#         # data = serializers.serialize('json', Product.objects.all())
#         data = {'products': Product.objects.all()}
#         return Response(data, template_name='basket/index.html')
from django.shortcuts import render
from .models import Product, Photo, Basket

# Create your views here.

#main page view
def index(request):
    title = 'Index page'
    content = {
        'title': title
    }
    return render(request, 'basket/index.html', content)
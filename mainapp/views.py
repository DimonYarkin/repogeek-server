from django.shortcuts import render
from datetime import date
from mainapp.models import Product, ProductCategory


# Create your views here.
def index(request):
    context = {'title': 'geek shop',
               'to_day': date.today()
               }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'geekShop - product',
        'to_day': date.today(),
        'produts': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }

    return render(request, 'mainapp/products.html', context)

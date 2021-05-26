from django.shortcuts import render
from datetime import date
from mainapp.models import Product, ProductCategory

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import ListView

# Create your views here.
def index(request):
    context = {'title': 'geek shop',
               'to_day': date.today()
               }
    return render(request, 'mainapp/index.html', context)


def products(request, category_id=None, page=1):
    context = {'title': 'GeekShop - Каталог',
               'categories': ProductCategory.objects.all(),
               'to_day': date.today(),
               }
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    paginator = Paginator(products, per_page=3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context.update({'products': products_paginator})
    return render(request, 'mainapp/products.html', context)

class ContactListView(ListView):
    paginate_by = 3
    model = Product
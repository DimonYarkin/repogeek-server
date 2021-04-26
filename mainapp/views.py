from django.shortcuts import render
from datetime import date


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
        'produts': [
            {'card_img_top': 'Adidas-hoodie.png',
             'card_title': 'Худи черного цвета с монограммами adidas Originals',
             'price': 6090.00,
             'card_text': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'card_img_top': 'Blue-jacket-The-North-Face.png',
             'card_title': 'Синяя куртка The North Face',
             'price': 23725.00,
             'card_text': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
            {'card_img_top': 'Brown-sports-oversized-top-ASOS-DESIGN.png',
             'card_title': 'Коричневый спортивный oversized-топ ASOS DESIGN',
             'price': 3390.00,
             'card_text': 'Материал с плюшевой текстурой. Удобный и мягкий.'},
            {'card_img_top': 'Black-Nike-Heritage-backpack.png',
             'card_title': 'Черный рюкзак Nike Heritage',
             'price': 2340.00,
             'card_text': 'Плотная ткань. Легкий материал.'},
            {'card_img_top': 'Black-Dr-Martens-shoes.png',
             'card_title': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'price': 13590.00,
             'card_text': 'Гладкий кожаный верх. Натуральный материал.'},
            {'card_img_top': 'Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
             'card_title': 'Темно-синие широкие строгие брюки ASOS DESIGN',
             'price': 2890.00,
             'card_text': 'Легкая эластичная ткань сирсакер Фактурная ткань.'}

        ]
    }

    return render(request, 'mainapp/products.html', context)

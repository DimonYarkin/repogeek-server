from django.urls import path

from mainapp.views import products,ProducttListView

app_name = 'mainapp'

urlpatterns = [
    path('', products, name='index'),
    path('<int:category_id>/', products, name='product'),
    # path('page/<int:page>/', products, name='page'),
    path('page/<int:page>/', ProducttListView.as_view(), name='page'),
]
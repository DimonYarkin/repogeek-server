from django.contrib import admin

# Register your models here.
from mainapp.models import ProductCategory, Product


# admin.site.register(Product)
# admin.site.register(ProductCategory)



@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'desription']
    fields = ('name', 'desription')
    #sort
    ordering = ['name']
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'price', 'category']
    fields = ('name', 'image', 'desription',('quantity', 'price'), 'category')
    # readonly_fields = ['desription']
    #sort
    ordering = ['-name']
    search_fields = ['name']
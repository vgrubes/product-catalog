from django.contrib import admin
from product_catalog.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
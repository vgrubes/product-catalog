from django.contrib import admin
from product_catalog.models import Product, Rating


class ProductAdmin(admin.ModelAdmin):
    pass


class RatingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Rating, RatingAdmin)

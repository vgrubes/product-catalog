from django.apps import AppConfig


class ProductCatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product_catalog'

    def ready(self):
        import product_catalog.signals


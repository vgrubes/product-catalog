from django.core.management import BaseCommand

from product_catalog.documents import ProductDocument


class Command(BaseCommand):

    def handle(self, *args, **options):
        products = ProductDocument.search().filter("term", name="1")

        for product in products:
            print('Product retrieved: ', product.name)

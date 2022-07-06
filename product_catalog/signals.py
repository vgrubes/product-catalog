from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_elasticsearch_dsl.registries import registry

from product_catalog.models import Rating, Product


@receiver(post_save, sender=Rating)
def update_average_product_rating(sender, instance, created, **kwargs):
    ratings = Rating.objects.filter(product=instance.product)
    rating_values = list(map(lambda rating: rating.value, ratings))
    average_rating = (sum(rating_values))/(len(rating_values))

    instance.product.average_rating = average_rating
    instance.product.save()


@receiver(post_save, sender=Product)
def update_document(sender, instance, **kwargs):
    registry.update(instance)


@receiver(post_delete, sender=Product)
def delete_document(sender, instance, **kwargs):
    registry.update(instance)

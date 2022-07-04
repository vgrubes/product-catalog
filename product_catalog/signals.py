from django.db.models.signals import post_save
from django.dispatch import receiver

from product_catalog.models import Rating


@receiver(post_save, sender=Rating)
def update_average_product_rating(sender, instance, created, **kwargs):
    ratings = Rating.objects.filter(product=instance.product)
    rating_values = list(map(lambda rating: rating.value, ratings))
    average_rating = sum(rating_values)/len(rating_values)

    instance.product.average_rating = average_rating
    instance.product.save()

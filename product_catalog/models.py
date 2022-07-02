from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(
        blank=False,
        null=False,
        unique=True,
        max_length=255
    )
    price = models.FloatField(blank=False, null=False)
    rating = models.FloatField(blank=False, null=False, validators=[
        MinValueValidator(0.0), MaxValueValidator(5.0)
    ])
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
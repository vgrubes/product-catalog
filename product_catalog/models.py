from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Product(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        unique=True,
        max_length=255
    )
    price = models.FloatField(blank=False, null=False)
    average_rating = models.FloatField(blank=True, null=True, validators=[
        MinValueValidator(0.0), MaxValueValidator(5.0)
    ])
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Rating(models.Model):
    value = models.FloatField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(0.0), MaxValueValidator(5.0)
        ]
    )
    user = models.ForeignKey(
        User,
        related_name='ratings',
        on_delete=models.CASCADE,
        null=False
    )
    product = models.ForeignKey(
        Product,
        related_name='ratings',
        on_delete=models.CASCADE,
        null=False
    )

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
        unique_together = ['user', 'product']

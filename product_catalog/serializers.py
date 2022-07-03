from django.contrib.auth.models import User
from rest_framework import serializers

from product_catalog.models import Product, Rating


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    ratings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'rating', 'updated_at', 'ratings']


class RatingSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Rating
        fields = ['id', 'rating', 'product', 'user']

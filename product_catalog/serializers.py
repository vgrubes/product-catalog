from django.contrib.auth.models import User
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers

from product_catalog.documents import ProductDocument
from product_catalog.models import Product, Rating


class ProductSerializer(serializers.ModelSerializer):
    ratings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    average_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'average_rating',
            'updated_at',
            'ratings'
        ]


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Rating
        fields = ['id', 'value', 'product', 'user']


class ProductDocumentSerializer(DocumentSerializer):

    class Meta:
        document = ProductDocument
        fields = ('name',)
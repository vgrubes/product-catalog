from django_elasticsearch_dsl_drf.filter_backends import \
    FilteringFilterBackend, IdsFilterBackend, OrderingFilterBackend, \
    DefaultOrderingFilterBackend, SearchFilterBackend
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from rest_framework import viewsets, permissions, status, filters
from rest_framework.response import Response

from product_catalog.documents import ProductDocument
from product_catalog.models import Product, Rating
from product_catalog.serializers import ProductSerializer, RatingSerializer, \
    ProductDocumentSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ['name', 'price', 'average_rating', 'updated_at']
    ordering = ['average_rating']


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        rating = {
            'value': request.data.get('value'),
            'user': self.request.user.id,
            'product': request.data.get('product')
        }

        serializer = self.get_serializer(data=rating)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class ProductDocumentViewSet(DocumentViewSet):

    document = ProductDocument
    serializer_class = ProductDocumentSerializer
    pagination_class = PageNumberPagination
    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]
    search_fields = ('name',)
    filter_fields = {
        'name': 'name.raw'
    }
    ordering_fields = {'name': 'name.raw'}

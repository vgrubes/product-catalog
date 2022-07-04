from rest_framework import viewsets, permissions, status, filters
from rest_framework.response import Response

from product_catalog.models import Product, Rating
from product_catalog.serializers import ProductSerializer, RatingSerializer


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

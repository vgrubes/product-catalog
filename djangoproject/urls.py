"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework.renderers import JSONOpenAPIRenderer

from product_catalog import views
from product_catalog.views import ProductDocumentViewSet

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'ratings', views.RatingViewSet)
router.register(r'search/products', ProductDocumentViewSet, basename="search")

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', get_schema_view(
        title="Product Catalog API",
        version="1.0",
        description="This is a basic example of OpenAPI schema generator "
                    "in JSON format",
        renderer_classes=[JSONOpenAPIRenderer]
    )),
    path('admin/', admin.site.urls),
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    )
]


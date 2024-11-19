from rest_framework import viewsets

from sale.models import Product, Sale
from sale import serializers
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = serializers.SaleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('date',)

    def create(self, request, *args, **kwargs):
        create_serializer = serializers.CreateSaleSerializer(data=request.data)
        create_serializer.is_valid(raise_exception=True)
        self.perform_create(create_serializer)
        serializer = self.get_serializer(create_serializer.instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


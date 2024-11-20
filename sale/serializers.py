from rest_framework import serializers
from sale.models import Product, Sale, SaleProduct
from sale.utils import create_sale


class ProductSerializer(serializers.ModelSerializer):
    iva=serializers.ModelField(model_field=Product()._meta.get_field('iva'), required=False)

    class Meta:
        model = Product
        fields = (
            "id",
            "code",
            "name",
            "price",
            "iva",
        )


class SaleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleProduct
        fields = (
            "product",
            "quantity",
        )


class CreateSaleSerializer(serializers.ModelSerializer):
    products = SaleProductSerializer(many=True)

    def validate_products(self, products):
        products_obj = []

        for product in products:
            product_obj = product["product"]
            if product_obj not in products_obj:
                products_obj.append(product_obj)
            else:
                raise serializers.ValidationError("The product is duplicated")

        return products

    def create(self, validated_data):
        return create_sale(validated_data)

    class Meta:
        model = Sale
        fields = (
            "consecutive",
            "date",
            "customer",
            "products",
        )


class SaleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleProduct
        fields = (
            "quantity",
            "code",
            "name",
            "price",
            "iva",
        )


class SaleSerializer(serializers.ModelSerializer):
    saleproduct_set = SaleProductSerializer(many=True)

    class Meta:
        model = Sale
        fields = (
            "consecutive",
            "date",
            "created_at",
            "customer",
            "subtotal",
            "iva",
            "saleproduct_set",
        )

class FilterDateSerializer(serializers.Serializer):
    date = serializers.DateField(required=False)
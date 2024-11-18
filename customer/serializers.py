from rest_framework import serializers
from customer.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            "email",
            "first_name",
            "last_name",
            "document_type",
            "document_number",
        )

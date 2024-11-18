from django.contrib.auth.models import Group, User
from rest_framework import generics
from customer.serializers import CustomerSerializer
from customer.models import Customer
from rest_framework import viewsets

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

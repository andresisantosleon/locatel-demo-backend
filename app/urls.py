from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path(
        "api/customer/",
        include(("customer.urls", "customer"), namespace="api_customer"),
    ),
    path(
        "api/sale/",
        include(("sale.urls", "sale"), namespace="api_sale"),
    ),
]

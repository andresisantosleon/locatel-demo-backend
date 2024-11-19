from django.urls import include, path
from rest_framework import routers

from sale import views

router = routers.DefaultRouter()
router.register(r"product", views.ProductViewSet)
router.register(r"sale", views.SaleViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

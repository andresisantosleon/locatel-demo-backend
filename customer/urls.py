from django.urls import include, path
from rest_framework import routers

from customer import views

router = routers.DefaultRouter()
router.register(r'customer', views.CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
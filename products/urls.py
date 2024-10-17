from django.urls import path, include
from rest_framework import routers

from products import views

router = routers.DefaultRouter()

router.register(r"generators", views.ProductViewSet)
router.register(r"batteries", views.BatteryViewSet)
router.register(r"inverters", views.InverterViewSet)
router.register(r"portablePowerStation", views.PortablePowerStationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "products"

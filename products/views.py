from rest_framework.viewsets import ModelViewSet

from products.models import Generator, Battery, Inverter, PortablePowerStation
from products.serializers import (
    GeneratorSerializer,
    BatterySerializer,
    InverterSerializer,
    PortablePowerStationSerializer
)
from products.permissions import ReadOnlyOrAdminPermissions


class ProductViewSet(ModelViewSet):
    serializer_class = GeneratorSerializer
    queryset = Generator.objects.all()
    permission_classes = [ReadOnlyOrAdminPermissions]


class BatteryViewSet(ModelViewSet):
    serializer_class = BatterySerializer
    queryset = Battery.objects.all()
    permission_classes = [ReadOnlyOrAdminPermissions]


class InverterViewSet(ModelViewSet):
    serializer_class = InverterSerializer
    queryset = Inverter.objects.all()
    permission_classes = [ReadOnlyOrAdminPermissions]


class PortablePowerStationViewSet(ModelViewSet):
    serializer_class = PortablePowerStationSerializer
    queryset = PortablePowerStation.objects.all()
    permission_classes = [ReadOnlyOrAdminPermissions]

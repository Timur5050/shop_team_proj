from rest_framework.viewsets import ModelViewSet

from products.models import Generator, Battery, Inverter, PortablePowerStation
from products.serializers import (
    GeneratorSerializer,
    BatterySerializer,
    InverterSerializer,
    PortablePowerStationSerializer
)


class ProductViewSet(ModelViewSet):
    serializer_class = GeneratorSerializer
    queryset = Generator.objects.all()


class BatteryViewSet(ModelViewSet):
    serializer_class = BatterySerializer
    queryset = Battery.objects.all()


class InverterViewSet(ModelViewSet):
    serializer_class = InverterSerializer
    queryset = Inverter.objects.all()


class PortablePowerStationViewSet(ModelViewSet):
    serializer_class = PortablePowerStationSerializer
    queryset = PortablePowerStation.objects.all()

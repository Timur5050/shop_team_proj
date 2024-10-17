from rest_framework import serializers

from products.models import Generator, Battery, Inverter, PortablePowerStation


class GeneratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generator
        fields = '__all__'


class BatterySerializer(serializers.ModelSerializer):
    class Meta:
        model = Battery
        fields = '__all__'


class InverterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inverter
        fields = '__all__'


class PortablePowerStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortablePowerStation
        fields = '__all__'

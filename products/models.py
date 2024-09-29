import uuid
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Generator(models.Model):
    title = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    nominal_power_rating = models.DecimalField(max_digits=4, decimal_places=2)
    maximum_power = models.DecimalField(max_digits=4, decimal_places=2)
    number_of_phases = models.CharField(max_length=255)
    type_of_start = models.CharField(max_length=255)
    execution = models.CharField(max_length=255)
    cooling_system = models.CharField(max_length=255)
    type_of_installation = models.CharField(max_length=255)
    machine_class = models.CharField(max_length=255)
    appointment_for = models.CharField(max_length=255)
    type_of_fuel = models.CharField(max_length=255)
    type_of_alternator = models.CharField(max_length=255)
    alternator_winding_material = models.CharField(max_length=255)
    equipment = models.CharField(max_length=255)
    country_of_origin_of_the_brand = models.CharField(max_length=255)
    power_factor = models.DecimalField(max_digits=3, decimal_places=2)
    voltage = models.IntegerField()
    frequency = models.IntegerField()
    rated_current_strength = models.DecimalField(max_digits=5, decimal_places=2)
    fuel_tank_capacity = models.DecimalField(max_digits=5, decimal_places=2)
    fuel_consumption_litres_hour = models.DecimalField(max_digits=4, decimal_places=2)
    engine_power_hp = models.DecimalField(max_digits=4, decimal_places=2)
    engine_displacement = models.DecimalField(max_digits=6, decimal_places=2)
    engine_speed_rpm = models.IntegerField()
    volume_of_oil_in_the_engine_crankcase_litres = models.DecimalField(max_digits=4, decimal_places=2)
    continuous_operation_time_hours = models.DecimalField(max_digits=4, decimal_places=2)
    availability_of_an_hour_meter = models.BooleanField()
    degree_of_protection = models.CharField(max_length=255)
    output_12_v = models.BooleanField()
    height_mm = models.DecimalField(max_digits=5, decimal_places=1)
    width_mm = models.DecimalField(max_digits=5, decimal_places=1)
    weight_kg = models.DecimalField(max_digits=6, decimal_places=2)
    warranty_months = models.IntegerField()
    additional_information = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    slug = models.SlugField(unique=True, editable=False)


class Battery(models.Model):
    title = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    nominal_voltage = models.DecimalField(max_digits=5, decimal_places=2)
    capacity_ah = models.DecimalField(max_digits=5, decimal_places=1)
    nominal_charge_current = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    maximum_charge_current = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    number_of_cycles = models.IntegerField(blank=True, null=True)
    operating_temperature = models.CharField(max_length=255, blank=True, null=True)

    height_mm = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    width_mm = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    depth_mm = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)

    warranty_months = models.IntegerField(blank=True, null=True)
    additional_information = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Inverter(models.Model):
    # Common fields for all inverters
    title = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    battery_type = models.CharField(max_length=255, blank=True, null=True)
    power_kw = models.DecimalField(max_digits=5, decimal_places=2)
    battery_voltage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    power_factor = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    input_phases = models.CharField(max_length=255, blank=True, null=True)
    output_phases = models.CharField(max_length=255, blank=True, null=True)

    # Voltage thresholds
    lower_input_voltage_threshold = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    upper_input_voltage_threshold = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    output_voltage = models.CharField(max_length=255, blank=True, null=True)

    # Frequency and current details
    grid_frequency_hz = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    max_input_current_a = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    grid_voltage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    charging_time_ms = models.IntegerField(blank=True, null=True)
    has_charger = models.BooleanField(default=False)

    # Environmental conditions
    operating_temperature = models.CharField(max_length=255, blank=True, null=True)
    humidity_percent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    degree_of_protection = models.CharField(max_length=255, blank=True, null=True)

    # Physical dimensions
    height_mm = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    width_mm = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    depth_mm = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    # Warranty
    warranty_months = models.IntegerField()

    # Execution type
    type_of_execution = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class PortablePowerStation(models.Model):
    # Common fields for both power stations
    title = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)  # e.g., LiFe, Konner&Sohnen
    nominal_power_w = models.DecimalField(max_digits=6, decimal_places=1)  # Nominal power in Watts, e.g., 1000 W, 100 W
    peak_power_w = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)  # Peak power in Watts
    battery_type = models.CharField(max_length=255)  # e.g., Lithium-ion
    ac_output_voltage_v = models.CharField(max_length=255, blank=True, null=True)  # AC Output voltage, e.g., 230V
    dc_output_voltage = models.CharField(max_length=255, blank=True, null=True)  # DC Output voltage range
    battery_capacity_wh = models.DecimalField(max_digits=6,
                                              decimal_places=1)  # Battery capacity in Watt-hours, e.g., 932Wh, 155Wh
    solar_charging_input = models.BooleanField(default=False)  # Whether it supports solar charging
    solar_charging_input_spec = models.CharField(max_length=255, blank=True,
                                                 null=True)  # Specifications for solar charging, if available
    working_temperature_range = models.CharField(max_length=255)  # Operating temperature, e.g., -10°C to +40°C

    # Physical dimensions and weight
    height_mm = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)  # Height in mm
    width_mm = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)  # Width in mm
    depth_mm = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)  # Depth in mm
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # Weight in kg

    # Warranty information
    warranty_months = models.IntegerField()  # Warranty period in months

    # Charging and output details
    usb_output_qc = models.CharField(max_length=255, blank=True, null=True)  # USB output with Quick Charge specs
    type_c_output = models.CharField(max_length=255, blank=True, null=True)  # Type-C output specs
    ac_output_spec = models.CharField(max_length=255, blank=True,
                                      null=True)  # AC output specifications (e.g., Schuko 230V/50Hz)
    dc_output_spec = models.CharField(max_length=255, blank=True, null=True)  # DC output specifications
    other_ports = models.CharField(max_length=255, blank=True,
                                   null=True)  # Other ports (e.g., Auto cigarette lighter, DC5525)

    # Additional features
    led_lamp = models.BooleanField(default=False)  # Whether it has a built-in LED lamp
    wireless_charging_power_w = models.DecimalField(max_digits=5, decimal_places=1, blank=True,
                                                    null=True)  # Wireless charging power in watts

    # Additional details
    additional_information = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

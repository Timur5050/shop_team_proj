import uuid
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Generator(models.Model):
    title = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    height_mm = models.DecimalField(max_digits=5, decimal_places=1)
    width_mm = models.DecimalField(max_digits=5, decimal_places=1)
    weight_kg = models.DecimalField(max_digits=6, decimal_places=2)
    voltage = models.IntegerField()
    frequency = models.IntegerField()
    engine_power_hp = models.DecimalField(max_digits=4, decimal_places=2)
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
    height_mm = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    width_mm = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    depth_mm = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    nominal_voltage = models.DecimalField(max_digits=5, decimal_places=2)
    number_of_cycles = models.IntegerField(blank=True, null=True)
    operating_temperature = models.CharField(max_length=255, blank=True, null=True)
    warranty_months = models.IntegerField(blank=True, null=True)
    additional_information = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Inverter(models.Model):
    title = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    battery_type = models.CharField(max_length=255, blank=True, null=True)
    power_kw = models.DecimalField(max_digits=5, decimal_places=2)
    battery_voltage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    height_mm = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    width_mm = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    depth_mm = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    output_voltage = models.CharField(max_length=255, blank=True, null=True)
    warranty_months = models.IntegerField()
    additional_information = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class PortablePowerStation(models.Model):
    title = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)  # e.g., LiFe, Konner&Sohnen
    nominal_power_w = models.DecimalField(max_digits=6, decimal_places=1)  # Nominal power in Watts, e.g., 1000 W, 100 W
    peak_power_w = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)  # Peak power in Watts
    battery_type = models.CharField(max_length=255)  # e.g., Lithium-ion
    height_mm = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)  # Height in mm
    width_mm = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)  # Width in mm
    depth_mm = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)  # Depth in mm
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # Weight in kg
    warranty_months = models.IntegerField()  # Warranty period in months
    additional_information = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

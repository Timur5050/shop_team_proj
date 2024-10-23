import os
import uuid
from django.db import models
from django.utils.text import slugify


# Function to generate a dynamic image upload path
def get_image_path(instance, filename):
    """Generate a unique image upload path."""
    # Generates a unique filename using uuid
    ext = filename.split('.')[-1]
    # Use the instance's class name to dynamically set the folder and a unique name
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join(f"{instance.__class__.__name__.lower()}/images/", filename)


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
    image = models.ImageField(upload_to=get_image_path, null=True, blank=True)  # Updated to use dynamic path
    additional_information = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


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
    image = models.ImageField(upload_to=get_image_path, null=True, blank=True)  # Updated to use dynamic path
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
    image = models.ImageField(upload_to=get_image_path, null=True, blank=True)  # Updated to use dynamic path
    additional_information = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class PortablePowerStation(models.Model):
    title = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    nominal_power_w = models.DecimalField(max_digits=6, decimal_places=1)
    peak_power_w = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    battery_type = models.CharField(max_length=255)
    height_mm = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    width_mm = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    depth_mm = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    warranty_months = models.IntegerField()
    image = models.ImageField(upload_to=get_image_path, null=True, blank=True)  # Updated to use dynamic path
    additional_information = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

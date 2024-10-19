# Generated by Django 5.1.1 on 2024-10-19 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_portablepowerstation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='battery',
            name='capacity_ah',
        ),
        migrations.RemoveField(
            model_name='battery',
            name='maximum_charge_current',
        ),
        migrations.RemoveField(
            model_name='battery',
            name='nominal_charge_current',
        ),
        migrations.RemoveField(
            model_name='generator',
            name='alternator_winding_material',
        ),
        migrations.RemoveField(
            model_name='generator',
            name='appointment_for',
        ),
        migrations.RemoveField(
            model_name='generator',
            name='availability_of_an_hour_meter',
        ),
        migrations.RemoveField(
            model_name='generator',
            name='continuous_operation_time_hours',
        ),
        migrations.RemoveField(
            model_name='generator',
            name='cooling_system',
        ),
        migrations.RemoveField(
            model_name='generator',
            name='country_of_origin_of_the_brand',
        ),
        migrations.RemoveField(
            model_name='generator',
            name='degree_of_protection',
        ),
        migrations.RemoveField(
            model_name='generator',
            name='engine_displacement',
        ),
        migrations.RemoveField(
            model_name='generator',
            name='engine_speed_rpm',
        ),
        migrations.RemoveField(
            model_name='generator',
            name='equipment',
        ),
        migrations.RemoveField(
            model_name='generator',
            name='execution',
        ),
        migrations.RemoveField(
            model_name='generator',
            name='fuel_consumption_litres_hour',
        ),
        migrations.RemoveField(
            model_name='generator',
            name='fuel_tank_capacity',
        ),
        migrations.RemoveField(
            model_name='generator',
            name='machine_class',
        ),
        migrations.RemoveField(
            model_name='generator',
            name='maximum_power',
        ),
        migrations.RemoveField(
            model_name='generator',
            name='nominal_power_rating',
        ),
        migrations.RemoveField(
            model_name='generator',
            name='number_of_phases',
        ),
        migrations.RemoveField(
            model_name='generator',
            name='output_12_v',
        ),
        migrations.RemoveField(
            model_name='generator',
            name='power_factor',
        ),
        migrations.RemoveField(
            model_name='generator',
            name='rated_current_strength',
        ),
        migrations.RemoveField(
            model_name='generator',
            name='type_of_alternator',
        ),
        migrations.RemoveField(
            model_name='generator',
            name='type_of_fuel',
        ),
        migrations.RemoveField(
            model_name='generator',
            name='type_of_installation',
        ),
        migrations.RemoveField(
            model_name='generator',
            name='type_of_start',
        ),
        migrations.RemoveField(
            model_name='generator',
            name='volume_of_oil_in_the_engine_crankcase_litres',
        ),
        migrations.RemoveField(
            model_name='inverter',
            name='charging_time_ms',
        ),
        migrations.RemoveField(
            model_name='inverter',
            name='degree_of_protection',
        ),
        migrations.RemoveField(
            model_name='inverter',
            name='grid_frequency_hz',
        ),
        migrations.RemoveField(
            model_name='inverter',
            name='grid_voltage',
        ),
        migrations.RemoveField(
            model_name='inverter',
            name='has_charger',
        ),
        migrations.RemoveField(
            model_name='inverter',
            name='humidity_percent',
        ),
        migrations.RemoveField(
            model_name='inverter',
            name='input_phases',
        ),
        migrations.RemoveField(
            model_name='inverter',
            name='lower_input_voltage_threshold',
        ),
        migrations.RemoveField(
            model_name='inverter',
            name='max_input_current_a',
        ),
        migrations.RemoveField(
            model_name='inverter',
            name='operating_temperature',
        ),
        migrations.RemoveField(
            model_name='inverter',
            name='output_phases',
        ),
        migrations.RemoveField(
            model_name='inverter',
            name='power_factor',
        ),
        migrations.RemoveField(
            model_name='inverter',
            name='type_of_execution',
        ),
        migrations.RemoveField(
            model_name='inverter',
            name='upper_input_voltage_threshold',
        ),
        migrations.RemoveField(
            model_name='portablepowerstation',
            name='ac_output_spec',
        ),
        migrations.RemoveField(
            model_name='portablepowerstation',
            name='ac_output_voltage_v',
        ),
        migrations.RemoveField(
            model_name='portablepowerstation',
            name='battery_capacity_wh',
        ),
        migrations.RemoveField(
            model_name='portablepowerstation',
            name='dc_output_spec',
        ),
        migrations.RemoveField(
            model_name='portablepowerstation',
            name='dc_output_voltage',
        ),
        migrations.RemoveField(
            model_name='portablepowerstation',
            name='led_lamp',
        ),
        migrations.RemoveField(
            model_name='portablepowerstation',
            name='other_ports',
        ),
        migrations.RemoveField(
            model_name='portablepowerstation',
            name='solar_charging_input',
        ),
        migrations.RemoveField(
            model_name='portablepowerstation',
            name='solar_charging_input_spec',
        ),
        migrations.RemoveField(
            model_name='portablepowerstation',
            name='type_c_output',
        ),
        migrations.RemoveField(
            model_name='portablepowerstation',
            name='usb_output_qc',
        ),
        migrations.RemoveField(
            model_name='portablepowerstation',
            name='wireless_charging_power_w',
        ),
        migrations.RemoveField(
            model_name='portablepowerstation',
            name='working_temperature_range',
        ),
        migrations.AddField(
            model_name='inverter',
            name='additional_information',
            field=models.TextField(blank=True, null=True),
        ),
    ]
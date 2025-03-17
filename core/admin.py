from django.contrib import admin

from django.contrib import admin
from .models import Node, Sensor, Actuator

class SensorInline(admin.TabularInline):
    model = Sensor
    extra = 1  # Allows adding multiple sensors inline

class ActuatorInline(admin.TabularInline):
    model = Actuator
    extra = 1  # Allows adding multiple actuators inline

@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [SensorInline, ActuatorInline]  # Add sensors & actuators inline

admin.site.register(Sensor)
admin.site.register(Actuator)


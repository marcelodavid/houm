# django
from django.contrib import admin
from django.contrib.gis.db import models

# models
from houm.properties.models import Property

# widgets
from mapwidgets.widgets import GooglePointFieldWidget


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    """Properties admin"""
    formfield_overrides = {models.PointField: {"widget": GooglePointFieldWidget}}
    list_display = ("name", "direction", "number", "location")
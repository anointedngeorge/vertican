from django.contrib import admin
from django.shortcuts import render
from django.core import serializers
from io import BytesIO
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.template.loader import get_template
import csv
import json
import os
import importlib


def ActivatePassword(modeladmin, request, queryset):
    for obj in queryset:
        obj.set_password(obj.password)
        obj.save()
ActivatePassword.short_description = "Activate Password"
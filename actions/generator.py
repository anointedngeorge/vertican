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
from plugins.generator import generator

def codeGenerator(modeladmin, request, queryset):
    for x in queryset:
        if x.code == None:
            x.code = generator()
            x.save()
codeGenerator.short_description = "Assign Code"
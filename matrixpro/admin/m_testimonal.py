from django.contrib import admin
from matrixpro.models import *

from django.urls import path
from django.utils import timezone
from django.http import HttpResponse
from plugins.file_reader import (
    csvWriterMultipleRow, reader
)
import os


@admin.register(MatriproTestimonal)
class MatriproTestimonalAdmin(admin.ModelAdmin):
    list_display = ['title','control','created']
    # exclude=['status']

    
    
from django.contrib import admin
from matrixpro.models import *

from django.urls import path
from django.utils import timezone
from django.http import HttpResponse
from plugins.file_reader import (
    csvWriterMultipleRow, reader
)
import os


@admin.register(MatriproxBlog)
class MatriproxBlogAdmin(admin.ModelAdmin):
    list_display = ['title','image_thumbnail','posted_by','created']
    # exclude=['status']

    
    
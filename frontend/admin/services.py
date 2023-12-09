from django.contrib import admin
from frontend.models import *


@admin.register(ServicesModel)
class ServiceAdmin(admin.ModelAdmin):
    pass

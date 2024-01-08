from django.contrib import admin
from frontend.models import *


@admin.register(Television)
class TelevisionAdmin(admin.ModelAdmin):
    pass


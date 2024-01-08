from django.contrib import admin
from frontend.models import *


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass

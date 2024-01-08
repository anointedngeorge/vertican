from django.contrib import admin
from frontend.models import *


@admin.register(AboutModel)
class AboutAdmin(admin.ModelAdmin):
    pass

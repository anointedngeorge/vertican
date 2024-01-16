from django.contrib import admin
from frontend.models import *


@admin.register(FrontendImage)
class FrontendImageAdmin(admin.ModelAdmin):
    list_display=FRONTEND_IMAGE_DISPLAY

from django.contrib import admin
from frontend.models import *
from frontend.models.widgets import *

@admin.register(FooterWidgets)
class WidgetAdmin(admin.ModelAdmin):
    list_display = WIDGET_LIST_DISPLAY

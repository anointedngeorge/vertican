from django.contrib import admin
from frontend.models import *

@admin.register(FrontEndAgent)
class FrontEndAgentAdmin(admin.ModelAdmin):
    list_display = FRONTEND_AGENT_DISPLAY
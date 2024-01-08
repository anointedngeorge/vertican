from django.contrib import admin
from frontend.models import *


@admin.register(Downloads)
class DownloadAdmin(admin.ModelAdmin):
    pass

@admin.register(DownloadContent)
class DownloadContentAdmin(admin.ModelAdmin):
    pass

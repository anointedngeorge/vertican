from django.contrib import admin
from frontend.models import *


@admin.register(YoutubeModel)
class YoutubeAdmin(admin.ModelAdmin):
    pass

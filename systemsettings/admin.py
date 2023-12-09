from django.contrib import admin
from systemsettings.models import Media

# Register your models here.

admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    pass
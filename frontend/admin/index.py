from django.contrib import admin
from frontend.models import *
from frontend.models.menus import *


@admin.register(SettingModel)
class SettingAdmin(admin.ModelAdmin):
    pass


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display =  SLIDER_LIST_DISPLAY



@admin.register(MenusModel)
class MenuModelAdmin(admin.ModelAdmin):
    list_display =  MenusModel_list
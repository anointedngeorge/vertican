from django.contrib import admin
from frontend.models import *


@admin.register(MenusModel)
class MenuModelAdmin(admin.ModelAdmin):
    list_display =  MenusModel_list

@admin.register(MenuChildModel)
class MenuChildModelAdmin(admin.ModelAdmin):
    pass

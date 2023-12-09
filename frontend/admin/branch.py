from django.contrib import admin
from frontend.models import *


@admin.register(BranchModel)
class BranchAdmin(admin.ModelAdmin):
    pass

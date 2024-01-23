from django.db import models
from django.core.exceptions import ValidationError

from core.core import CoreBaseModel
from frontend.singleton.setting_singleton import *
from ckeditor.fields import RichTextField
# Create your models here.







WIDGET_LIST_DISPLAY = ['widgetID','isActive']

class FooterWidgets(CoreBaseModel):
    widgetID =  models.CharField(max_length=100) 
    widget =  RichTextField(null=True, blank=True)
    isActive = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.widgetID}"
    

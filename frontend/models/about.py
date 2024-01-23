from django.db import models
from django.core.exceptions import ValidationError

from core.core import CoreBaseModel
from frontend.singleton.setting_singleton import *
from ckeditor.fields import RichTextField
# Create your models here.


class AboutModel(CoreBaseModel):
    about = RichTextField(null=True, blank=True)
    # site_logo = models.ImageField(upload_to='/contact', null=True, blank=True)
    # site_title = models.CharField(max_length=250, null=True, blank=True)
    # site_subtitle = models.CharField(max_length=250, default="", blank=True)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

    def __str__(self) -> str:
        return f"{self.id}"
    
    def clean(self):
        # Ensure there is only one instance
        if AboutModel.objects.exclude(pk=self.pk).exists():
            raise ValidationError("Only one instance of YourModel is allowed.")




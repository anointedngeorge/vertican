from django.db import models
from core.core import CoreBaseModel
from frontend.singleton.setting_singleton import *
# Create your models here.


class Television(CoreBaseModel):
    title = models.CharField(max_length=250, null=True, blank=True)
    youtube = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Television'
        verbose_name_plural = 'Televisions'

    def __str__(self) -> str:
        return f"{self.title}"

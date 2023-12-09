from django.db import models
from frontend.singleton.setting_singleton import *
# Create your models here.


class YoutubeModel(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    link = models.CharField(max_length=250, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Youtube Link'
        verbose_name_plural = 'Youtube Links'

    def __str__(self) -> str:
        return f"{self.title}"



from django.db import models
from frontend.singleton.setting_singleton import *
# Create your models here.


class AboutModel(models.Model):
    image = models.ImageField(upload_to='contact')



    class Meta:
        verbose_name = 'Branche'
        verbose_name_plural = 'Branches'

    def __str__(self) -> str:
        return f"{self.name}"



from django.db import models
from frontend.singleton.setting_singleton import *
# Create your models here.


class BranchModel(models.Model):
    image = models.ImageField(upload_to='contact')
    office = models.CharField(max_length=250, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    tel = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Branche'
        verbose_name_plural = 'Branches'

    def __str__(self) -> str:
        return f"{self.office}"



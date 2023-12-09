from django.db import models
from frontend.singleton.setting_singleton import *
# Create your models here.


MenusModel_list = ['title','link','has_children']
class MenusModel(models.Model):

    title = models.CharField(max_length=250, null=True, blank=True)
    link = models.CharField(max_length=250, null=True, blank=True)
    has_children = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self) -> str:
        return f"{self.title}"



from django.db import models
from core.core import CoreBaseModel
from frontend.singleton.setting_singleton import *
# Create your models here.


def getMenusLinks():
    container  = [(f"/", "Index")]
    import os
    p = "frontend/templates/property"
    PATH_EXISTS = os.path.exists(p)
    if PATH_EXISTS:
        container += [(f"/{f}".split(".")[0], str(str(f).split(".")[0].replace("_", " ")).upper()) for f in os.listdir(p) if f.endswith('.html')]
    return container

print(getMenusLinks())
MenusModel_list = ['title','link','has_children']
class MenusModel(CoreBaseModel):
    title = models.CharField(max_length=250, null=True, blank=True)
    link = models.CharField(max_length=250, null=True, blank=True, choices=getMenusLinks())
    index = models.IntegerField(default=0)
    has_children = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self) -> str:
        return f"{self.title}"



class MenuChildModel(CoreBaseModel):
    menu = models.ForeignKey('frontend.MenusModel', on_delete=models.CASCADE, related_name="menu")
    title = models.CharField(max_length=250, null=True, blank=True)
    link = models.CharField(max_length=250, null=True, blank=True)
    index = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = 'Menu Child'
        verbose_name_plural = 'Menu Children'
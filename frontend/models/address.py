from django.db import models
from core.core import CoreBaseModel


class Address(CoreBaseModel):
    POSITION_CHOICE = [
        ("left", "left"),
        ("right", "right"),
    ]
    
    icon = models.CharField(max_length=150)
    title = models.CharField(max_length=150, null=True, blank=True)
    link = models.CharField(max_length=150, blank=True, default="")
    index = models.IntegerField(default=0)
    position = models.CharField(max_length=150, choices=POSITION_CHOICE)
    
    def __str__(self):
        return self.icon
    
    class Meta:
        verbose_name_plural = "Addresses"
    
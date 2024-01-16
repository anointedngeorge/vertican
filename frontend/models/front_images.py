from django.db import models
from django.core.exceptions import ValidationError

from core.core import CoreBaseModel
# Create your models here.

FRONTEND_IMAGE_DISPLAY = ['id', 'title', 'alt']
class FrontendImage(CoreBaseModel):
    image = models.ImageField(upload_to='frontendImages', null=True, blank=True)
    title = models.CharField(max_length=250, default="", blank=True)
    alt = models.CharField(max_length=250, default="Image", blank=True)



    class Meta:
        verbose_name = 'Frontend Image'
        verbose_name_plural = 'Frontend Images'

    def __str__(self) -> str:
        return f"{self.id}"




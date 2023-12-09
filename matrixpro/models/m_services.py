from django.db import models
from core.core import CoreBaseModelWithImage
from ckeditor.fields import RichTextField

class MatriproxServices(CoreBaseModelWithImage):
    content =  RichTextField( )
    title = models.CharField(max_length=200, null=True, blank=False)
    index = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Our Service'
        verbose_name_plural = 'Our Services'

    def __str__(self) -> str:
        return f"{self.title}"




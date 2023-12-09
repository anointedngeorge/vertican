from django.db import models
from core.core import *
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.conf import settings


class MatriproxBlog(CoreBaseModel):
    content =  RichTextField( )
    status = models.BooleanField(default=False, choices=[(False, 'Reject'), (True,'Approve')] )
    commented_by = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Blog Comment'
        verbose_name_plural = 'Blog Comments'

    def __str__(self) -> str:
        return f"{self.title}"

# Waec!d1992!



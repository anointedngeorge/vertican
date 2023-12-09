from django.db import models
from core.core import CoreBaseModelWithImage
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.conf import settings
class MatriproxBlog(CoreBaseModelWithImage):
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(240, 190)],
        format='JPEG',
        options={'quality': 70}
    )
    content =  RichTextField( )
    title = models.CharField(max_length=200, null=True, blank=False)
    status = models.BooleanField(default=False, choices=[(False, 'Reject'), (True,'Approve')] )
    index = models.IntegerField(default=1)
    posted_by = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Our Blog'
        verbose_name_plural = 'Our Blog'

    def __str__(self) -> str:
        return f"{self.title}"




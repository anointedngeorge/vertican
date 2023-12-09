from django.db import models
from core.core import CoreBaseModel
from ckeditor.fields import RichTextField


class MatriproTestimonal(CoreBaseModel):
    client = models.ForeignKey("clients.MatrixClient", on_delete=models.CASCADE)
    content =  RichTextField()
    title = models.CharField(max_length=200, null=True, blank=False)
    control = models.BooleanField( default=False, choices=[(False,"Don't Show"), (True, "Show")] )

    class Meta:
        verbose_name = 'Testimonal'
        verbose_name_plural = 'Testimonals'

    def __str__(self) -> str:
        return f"{self.title}"


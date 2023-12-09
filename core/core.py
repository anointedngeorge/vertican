from django.db import models
import uuid
from django.utils import timezone
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
import os
import uuid
from authuser.models import User
class CoreBaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created=  models.DateField(auto_created=True, default=timezone.now, editable=False)
    
    
    class Meta:
        abstract = True




def uuidfilename(instance, filename):
    extension = filename.split('.')[-1]
    unique_filename = f"{uuid.uuid4()}.{extension}"
    return os.path.join('images/', unique_filename)


class CoreBaseModelWithImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateField(auto_created=True, default=timezone.now, editable=False)
    # add image
    image = models.ImageField(upload_to=uuidfilename, blank=True, null=True)
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(500, 100)],
        format='JPEG',
        options={'quality': 70}
    )
    
    class Meta:
        abstract = True




from django.db import models
from django.conf import settings
# Create your models here.



def ImageValidator(value):
    import os
    from django.core.exceptions import ValidationError
    from PIL import Image

    # Get the file extension
    ext = os.path.splitext(value.name)[1].lower()

    # Check if the file extension is not an image format
    if ext not in ['.jpg', '.jpeg', '.png', '.gif']:
        raise ValidationError('Only image files (jpg, jpeg, png, gif) are allowed.')

    # You can also check the image content to ensure it's a valid image
    try:
        with Image.open(value) as img:
            img.verify()
    except Exception:
        raise ValidationError('Invalid image file.')


class Media(models.Model):
    image = models.ImageField(upload_to='images/', validators=[ImageValidator])
    owner =  models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Media'
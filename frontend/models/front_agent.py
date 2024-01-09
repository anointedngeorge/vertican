from core.core import CoreBaseModel
from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image

def validate_square_image(value):
    if value:
        image = Image.open(value)
        width, height = image.size
        if width != height or width < 250 or height < 250:
            raise ValidationError('Image must be a square with dimensions at least 250x250 pixels.')



FRONTEND_AGENT_DISPLAY = ['first_name', 'last_name', 'role']
class FrontEndAgent(models.Model):
    first_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    role = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="frontend/agent", blank=True, validators=[validate_square_image])
    facebook_url = models.CharField(max_length=250, blank=True, default="#")
    twitter_url = models.CharField(max_length=250, blank=True, default="#")
    linkedin_url = models.CharField(max_length=250, blank=True, default="#")
    instagram_url = models.CharField(max_length=250, blank=True, default="#")
    
    class Meta:
        verbose_name = "Front End Agent"
        verbose_name_plural = "Front End Agents"
        
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    
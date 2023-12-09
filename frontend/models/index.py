from django.db import models
from frontend.singleton.setting_singleton import *
from choices import SliderActiveChoice,SliderShowOnlineChoice
# Create your models here.



SLIDER_LIST_DISPLAY = ['title','subtitle','alt','is_active','is_showed']
class Slider(models.Model):
    title = models.CharField(max_length=250, null=True)
    subtitle = models.CharField(max_length=250, null=True)
    alt = models.CharField(max_length=250, default='1.jpg')
    image = models.ImageField(upload_to="slider")
    is_media_file_online = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False, 
                                    choices=SliderActiveChoice.choices, help_text='Set one to true')
    is_showed = models.BooleanField(default=True, 
                                    choices=SliderShowOnlineChoice.choices, 
                                    help_text='Tell if to show on the website')
    
    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'
    

    def __str__(self) -> str:
        return f"{self.title}"
    



class SettingModel(SettingSingletonModelMixin, SettingSingletonModel):
      
    class Meta:
        verbose_name = 'Setting'
        verbose_name_plural = 'Settings'

    def __str__(self) -> str:
        return f"{self.tel} - {self.email}"



class ServicesModel(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    subtitle = models.CharField(max_length=250, null=True, blank=True)
    descriptions = models.TextField()
    ICON = [
        ('fa-gear','Gear'),
        ('fa-building-o', 'Building'),
        ('fa-home','Home')
    ]
    icon = models.CharField(max_length=300, choices=ICON, null=True)
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self) -> str:
        return f"{self.title}"


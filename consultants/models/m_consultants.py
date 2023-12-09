from django.db import models
from django.utils import timezone
from django.conf import settings
from django_countries.fields import CountryField
from authuser.models.user_model import User
from core.core import *
import uuid

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


ADMIN_LIST_DISPLAY = ['id','username','sponsor','uplink','first_name','last_name','country','email',
    'phone','status']

class ConsultantClass(models.Model):
    pass

def uuidfilename(instance, filename):
    extension = filename.split('.')[-1]
    unique_filename = f"{uuid.uuid4()}.{extension}"
    return os.path.join('images/', unique_filename)


class Consultant(User):
    first_name = models.CharField(max_length = 150, null=True)
    last_name = models.CharField(max_length = 150, null=True)
    profile = models.ImageField(upload_to=uuidfilename, blank=True, null=True)
    image_thumbnail = ImageSpecField(
        source='profile',
        processors=[ResizeToFill(500, 100)],
        format='JPEG',
        options={'quality': 70}
    )
    sponsor = models.ForeignKey("consultants.Consultant", on_delete=models.CASCADE, 
                                null=True, blank=True, error_messages='No match found')
    
    uplink = models.CharField(max_length = 150, blank=True, null=True)
    country = CountryField(blank_label="(Select Country)", default='---', 
    max_length=200, null=True)

    ac_no = models.CharField(max_length = 150, verbose_name='Account Number', blank=True, null=True)
    ac_name = models.CharField(max_length = 150, verbose_name='Account Name', blank=True, null=True)
    ac_type = models.CharField(max_length = 150, verbose_name='Account Type', blank=True, null=True)
    bank_name = models.CharField(max_length = 150, verbose_name='Account Type', blank=True, null=True)
    transaction_password = models.CharField(max_length = 150, blank=True, null=True)
    phone = models.CharField(max_length = 150, null=True)
    phone2 = models.CharField(max_length = 150, blank=True, null=True)
    dob = models.CharField(max_length = 150, blank=True, null=True)
    addr = models.CharField(max_length = 150, verbose_name='address', blank=True, null=True)
    descr = models.CharField(max_length = 150, verbose_name='description', blank=True, null=True)
    status = models.CharField(max_length = 150, choices=[
        ('blocked','Blocked'),
        ('unblocked','Unblocked')
    ], default='unblocked')
    type = models.CharField(max_length = 150, blank=True, null=True)
    my_wallet = models.CharField(max_length = 150, blank=True, null=True)
    add_date = models.DateField(auto_now=True, editable=False, null=True)
    sharable_link = models.CharField(max_length = 150, null=True, blank=True)
    # created  = models.DateField(auto_now=True)
    

    class Meta:
        verbose_name = 'Consultant'
        verbose_name_plural = 'Consultants'
        
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def get_model_name(self):
        return f"{self._meta.model.__name__}"
    

    def _sharable_link(self):
        link =  f""
        return 'xx'
    
    def save(self, *args, **kwargs):
        self.username = self.email.split("@")[0] if self.username is not None else self.username
        if not len(self.password) > 20:
            super().set_password(self.password)
            self.is_active = True
            self.is_staff = True
        return super().save(*args, **kwargs)

    

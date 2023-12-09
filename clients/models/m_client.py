from django.db import models
from authuser.models import User
from django_countries.fields import CountryField
from core.core import *

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class GetOrNoneManager(models.Manager):
    """Adds get_or_none method to objects
    """
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            n = self.model.__name__
            return f"Data not found on {n}"


ADMIN_CLIENT_LIST_DISPLAY = ['pk','surname', 'first_name', 'last_name','phone','occupation','c_sex']


class MatrixClient(User):
    # objects = GetOrNoneManager()
    surname = models.CharField(max_length = 200, null=True, default='-')
    first_name = models.CharField(max_length = 200, null=True, default='-')
    last_name = models.CharField(max_length = 200, null=True, default='-')
    profile = models.ImageField(upload_to=uuidfilename, blank=True, null=True)
    image_thumbnail = ImageSpecField(
        source='profile',
        processors=[ResizeToFill(500, 100)],
        format='JPEG',
        options={'quality': 70}
    )
    occupation = models.CharField(max_length = 200, null=True, default='-')
    c_sex = models.CharField(max_length = 200, verbose_name='gender', 
                             choices=[('male','Male'),('female','Female')])
    kin_name = models.CharField(max_length = 200, null=True, default='-')
    kin_phone = models.CharField(max_length = 200, null=True, default='-')
    phone = models.CharField(max_length = 200, null=True, default='-')
    kin_address = models.CharField(max_length = 200, null=True, default='-')
    nationality = CountryField(null=True, default='-')
    state = models.CharField(max_length = 200, null=True, default='-')
    address = models.CharField(max_length = 200, null=True, default='-')
    add_date = models.DateField(auto_now=True, editable=False, null=True)


    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering= ('add_date',)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def action(self):
        from plugins.dropdown import table_dropdown
        data = [
            {"name":"Sales", "url":f"property-sales-report/", "modal":True},
        ]
        return table_dropdown(title="Choose", content=data )
    

    def save(self, *args, **kwargs):
        self.username = (
            self.email.split("@")[0] if self.username is not None else self.username
        )
        if not len(self.password) > 20:
            super().set_password(self.password)
            self.is_active = True
            self.is_staff = True
        return super().save(*args, **kwargs)
    
    
    
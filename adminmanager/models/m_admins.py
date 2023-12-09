from django.db import models
from authuser.models import User
from django_countries.fields import CountryField




class GetOrNoneManager(models.Manager):
    """Adds get_or_none method to objects
    """
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            n = self.model.__name__
            return f"Data not found on {n}"


ADMIN_LIST_DISPLAY = ['surname', 'first_name', 'last_name','phone','c_sex']


class MatrixAdmin(User):
    surname = models.CharField(max_length = 200, null=True, default='-')
    first_name = models.CharField(max_length = 200, null=True, default='-')
    last_name = models.CharField(max_length = 200, null=True, default='-')
    profile_img = models.CharField(max_length = 250, null=True, blank=True)
    c_sex = models.CharField(max_length = 200, verbose_name='gender')
    phone = models.CharField(max_length = 200, null=True, default='-', blank=True)

    nationality = CountryField(blank_label="(Select Country)", default='---', 
    max_length=200, null=True)
    state = models.CharField(max_length = 200, null=True, default='-')
    add_date = models.DateField(auto_now=True, editable=False, null=True)


    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'
        ordering= ('add_date',)

    def __str__(self) -> str:
        return f"{self.surname} {self.first_name} {self.last_name}"
    
    
    
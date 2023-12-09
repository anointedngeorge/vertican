from django.db import models
from django.contrib.auth.models import Group, User
from django.contrib.auth.models import (
    AbstractBaseUser, 
    PermissionsMixin,
    BaseUserManager,
    UserManager
)
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
from plugins.dropdown import *


class Branch(models.Model):
    code = models.CharField(max_length = 150,blank=True, null=True)
    name = models.CharField(max_length = 150)
    country = CountryField(blank_label="(select country)", default='---', max_length=200)
    state = models.CharField(max_length=50, null=True, default='---')
    office_address = models.CharField(max_length=250, default='---')
    no_of_staff = models.CharField(max_length=250, default='---')
    branch_date = models.DateField(auto_now=True)
    description = models.TextField()
    
    class Meta:
        verbose_name = "branch"
        verbose_name_plural = "branch"

    def __str__(self) -> str:
        return f"{self.name}"




class BranchAccessories(models.Model):
    code = models.CharField(max_length = 150,blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True,
     related_name="related_branch")
    name = models.CharField(max_length = 150)
    assets_type  = models.CharField(max_length = 150,blank=True, null=True)
    value_of_asset = models.CharField(max_length = 150,blank=True, null=True)
    status = models.CharField(max_length = 150,blank=True, null=True,
    choices=[
        ('functioning','Functioning'),
        ('nonfunctioning','Non Functioning')
    ])
    description = models.TextField(blank=True, null=True)
    serial_number = models.CharField(max_length = 150)
    date_of_purchase = models.DateField(auto_now=False, default='2023-06-10')
    
    def action(self):
        modelname = self._meta.model.__name__
       
        action = {
            "soldout": [{"name":f"{self.code}", "href":f"", "is_button":False, 
                "query":{'id':self.id,'status':self.status,'title':self.name}},

            {"name":'sell', "href":f"", "is_button":False, 
                "query":{'id':self.id,'status':self.status,'title':self.name }},

            {"name":'sell', "href":f"", "is_button":False, 
                "query":{'id':self.id,'status':self.status,'title':self.name }}
            ],
            
            "avaliable": [],
        }
        return dictDropdown(action=action, status=self.status, modelname=modelname, code=self.code)

    class Meta:
        verbose_name = "Branch Accessories"
        verbose_name_plural = "Branch Accessories"

    def __str__(self) -> str:
        return f"{self.branch}"
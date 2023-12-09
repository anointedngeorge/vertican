from django.http import HttpResponse,JsonResponse
from django.core import serializers
import pandas as pd
import os
import datetime as dt
from datetime import datetime

from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template.response import TemplateResponse
from django.utils.html import format_html, html_safe
from django.utils.safestring import mark_safe
from django.urls import path
from django.urls import reverse
from django.conf import settings 
from django.contrib import messages
from authuser.models import User



def currentDateTime():
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d-%m-%Y_%H:%M:%S")
    return dt_string


def createAccount(modeladmin, request, queryset):
    try:
        counter = 1
        for x in queryset:
            username = f"{x.username}".replace(' ','').lower()
            email = f"{x.email}"
            data = {
                'first_name':x.first_name,
                'last_name':x.last_name,
                'email':email,
                'username':f"{username}",
                'password':x.password,
                'roles_name':'consultant'
            }
            User.objects.all().create(**data)
            x.username = username
            x.save()
            counter =  counter+1
    except Exception as e :
        return HttpResponse(e)
createAccount.short_description = "Create Account"

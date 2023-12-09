from typing import Any
from django.contrib import admin
from django.contrib.admin.sites import site
from django.db.models.query import QuerySet
from django.http import request
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.template.response import TemplateResponse
from django.urls import path
from authuser.models import * 
from authuser.forms import *
from django.shortcuts import render
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.html import format_html
from django.utils.safestring import mark_safe
# from etc.actions import *
import uuid
from django.http import HttpResponseRedirect
from django import template
# from django.utils.translation import ugettext as _
import random
import string

from import_export.admin import ImportExportModelAdmin
from actions.activate_password import (
    ActivatePassword
)


@admin.register(User)
class AuthModelAdmin(ImportExportModelAdmin):
    # search_fields = ['username__startswith', 'code__startswith']
    list_display = ['pk','username', 'email','roles','is_active']
    list_filter = ['username','email']
    # list_display_links = ['code']
    actions = [ActivatePassword]
    exclude = ['code','last_login','is_superuser','user_permissions','groups']
    # actions = [send_bulk_message, approve_bulk, reject_bulk]
    form = userRegistrationForm
    
    # def has_add_permission(self, request) -> bool:
    #     return False
    # def has_change_permission(self, request, obj=None) -> bool:
    #     return False
    

    def response_add(self, request, obj, post_url_continue=None) -> HttpResponse:
        # coded = str(uuid.uuid4()).replace("-", "")[:4]
        obj.set_password(obj.password)
        obj.is_active = True
        obj.save()
        return super().response_add(request, obj, post_url_continue)



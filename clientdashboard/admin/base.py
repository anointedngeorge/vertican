from typing import Any, Dict, List, Optional
from django.http import HttpResponse
from django.contrib import messages as mesage
from django.contrib import admin
from django.urls.resolvers import URLResolver
from django.urls import path, include, re_path
from django.template.response import TemplateResponse
from clientdashboard.forms.authentication import (
    CustomAuthenticationForm,
    AuthenticationRegisterForm
)
from authuser.models import *
from consultants.models import Consultant
from matrixpro.models import *
import os

CURRENT_TEMPLATE = 'client'
CURRENT_MAIN_TEMPLATE = 'clientdashboard'


# student/logout/
# student/password_change/
# <form method="post" id="login-form" action="{% url 'admin:login' %}">
# <form method="post" id="login-form" action="{% url 'admin:login' %}?next={{ request.GET.next }}">

class SuperadminDashboard(admin.AdminSite):
    site_title = 'Client Admin Interface'
    site_header = 'Client Dashboard'
    index_title = 'Client Dashboard'
    index_template = f'{CURRENT_TEMPLATE}/index.html'
    login_template = f'{CURRENT_TEMPLATE}/login.html'
    logout_template = f'{CURRENT_TEMPLATE}/logout.html'
    login_form = CustomAuthenticationForm
    

    def each_context(self, request):
        context = super().each_context(request)
        app_lists = self.get_app_list(request)
        

        context['title'] = self.site_title
        context['site_header'] = self.site_header
        context['index_title'] = self.index_title
        context['app_lists'] = app_lists
        context['property'] = {
            'sales': PropertySalesModel.objects.all().count(),
            'availableProperty':MatrixProperty.objects.all().count(),
            'featuredProperty':MatrixProperty.objects.all().count(),
            'consultant':Consultant.objects.all().count()
        }
        # this will set the current adminsite app that is running
        context['adminsite'] = self.name
        return context
    
    def get_urls(self) -> List[URLResolver]:
        urls = super().get_urls()
        add_urls = [
            path('profile/<str:id>/', self.profile, name='profile'),
        ]
        return add_urls + urls

    
    def profile(self, request, id=None):
        context = dict(self.each_context(request),)
        context['title'] = f"Profile {id} "
        context['site_header'] = f"Edit Profile"
        context['site_title'] = f"m"
        prop_model =  PropertySalesModel
        if request.user.is_superuser:
            context['viewobject'] = prop_model.objects.all()
        else: context['viewobject'] = prop_model.objects.all().filter(client_id=request.user.id)
        context['list_view'] = 'pk, consultant, pro_qty'

        return TemplateResponse(request, 'client/profile.html', context)


client_dashboard_site = SuperadminDashboard(name='client')



from typing import Any, Dict, List, Optional
from django.contrib.admin.options import InlineModelAdmin
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.contrib import admin
from django.forms import formset_factory
from django.contrib.admin.views.main import ChangeList
from django.http.request import HttpRequest
from django.urls.resolvers import URLPattern
from django.utils.html import format_html
from django.urls import reverse_lazy
from django.urls.resolvers import URLResolver
from django.urls import path, include, re_path
from django.template.response import TemplateResponse
import os

from authuser.models import User
from clients.models import *
# from consultants.models import Consultant
from matrixpro.models import PropertySalesModel

from clientdashboard.admin import CURRENT_MAIN_TEMPLATE,CURRENT_TEMPLATE,client_dashboard_site


# Register your models here using the student_site
class ClientCustomAdminsite(admin.ModelAdmin):
    list_display = ADMIN_CLIENT_LIST_DISPLAY
    list_display.insert(0, 'action')
    list_display_links = ['first_name']
    list_form = '__all__'
    exclude = [
        'user_permissions','code','last_login','password','username',
        'groups','is_active','is_staff','roles','is_superuser'
    ]
    # list_form = ['first_name','last_name']

    MODEL =  MatrixClient

    m = MODEL._meta
    
    template_list = os.path.realpath(f'{CURRENT_MAIN_TEMPLATE}/templates/{CURRENT_TEMPLATE}/{m.app_label}/{m.model_name}/change_list.html')
    template_form = os.path.realpath(f'{CURRENT_MAIN_TEMPLATE}/templates/{CURRENT_TEMPLATE}/{m.app_label}/{m.model_name}/change_form.html')

    delete_confirmation_template = template_list if os.path.exists(template_list) else f'{CURRENT_TEMPLATE}/delete_confirmation_template.html'
    # this will change the  change_list according to  apps
    change_list_template = template_list if os.path.exists(template_list) else f'{CURRENT_TEMPLATE}/change_list.html'
    # for change form
    change_form_template = template_form if os.path.exists(template_form) else f'{CURRENT_TEMPLATE}/change_form.html'


    def get_urls(self) -> List[URLResolver]:
        urls = super().get_urls()
        add_urls = [
            path('property-sales-report/', self.propertySalesReport, 
                 name='property-sales-report'),
        ]
        return add_urls + urls
    
    def propertySalesReport(self, request, client_id=None):
        context = dict(self.admin_site.each_context(request),)
        context['title'] = f"View {client_id} "
        context['site_header'] = f"View Page"
        context['site_title'] = f"{client_id}"
        prop_model =  PropertySalesModel
        if request.user.is_superuser:
            context['viewobject'] = prop_model.objects.all()
        else: context['viewobject'] = prop_model.objects.all().filter(client_id=request.user.id)
        context['list_view'] = 'pk, consultant, pro_qty'
        return TemplateResponse(request, 'templateResponse/propertySaleReport.html', context=context)
    

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(id=request.user.id)

   
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        from django.forms import modelform_factory
        # to import model form
        form = modelform_factory(self.model, fields=self.list_form, exclude=self.exclude)
        queryset =  self.get_queryset(request)
        
        if extra_context is None:
            extra_context = {}

        extra_context['referer'] = request.META.get('HTTP_REFERER')
        extra_context['form'] = form(request.POST or 
                                None, instance=queryset 
                                .filter(id=object_id).get()) if object_id else form
        
        return super().changeform_view(request, object_id, form_url, extra_context)

    def changelist_view(self, request, extra_context=None):
        model = self.model
        ModelFormSet = formset_factory(self.get_changelist_formset(request), extra=0)
        formset = ModelFormSet()

        sortable_by = self.get_sortable_by(request) 
        search_help_text = self.get_search_fields(request)
        
        for form in formset:
            form.queryset = model.objects.all()
        
        cl = ChangeList(request, self.model, self.list_display, self.list_display_links, self.list_filter,
                        self.date_hierarchy, self.search_fields, self.list_select_related,
                        self.list_per_page, self.list_max_show_all, self.list_editable, model_admin=self, sortable_by=sortable_by, search_help_text=search_help_text)
        
        opts =  cl.model._meta
        if extra_context is None:
            extra_context = {}
        extra_context['referer'] = request.META.get('HTTP_REFERER')
        extra_context['cl'] = cl
        extra_context['formset'] = formset
        extra_context['opts'] = opts
        extra_context['page_title'] = opts.verbose_name
        
        return super().changelist_view(request, extra_context=extra_context)
client_dashboard_site.register(MatrixClient, ClientCustomAdminsite)

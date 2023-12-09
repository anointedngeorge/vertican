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
from clients.models import MatrixClient
from consultants.models import Consultant
from matrixpro.models import *
from matrixpro.models.m_sales_details import ADMIN_LIST_DISPLAY_PROPERTYSALESMODEL, PropertySalesModel
# from matrixpro.models import 
from plugins.dropdown import table_dropdown
from clientdashboard.admin import CURRENT_MAIN_TEMPLATE,CURRENT_TEMPLATE,client_dashboard_site

from clientdashboard.forms.property import PropertyForm


# Register your models here using the student_site
class PropertiesAdminsite(admin.ModelAdmin):
    list_display = LIST_MatrixProperty
    list_display.insert(0, 'action')
    list_display_links = ['property_title']
    list_view = LIST_MatrixProperty_view
    list_form = '__all__'
  
    # list_form = ['first_name','last_name']

    MODEL =  MatrixProperty

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
            path('propertymedia/<str:id>/<str:name>/', self.propertymedia, name='propertymedia'),
            path('gallery/<str:id>/<str:name>/', self.gallery, name='gallery'),
            path('viewdata/<str:id>/', self.viewdata, name='viewdata'),
            path('googlemap/<str:id>/', self.googlemap, name='googlemap'),
        ]
        return add_urls + urls
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(client_id=request.user.id)
        
    
    def viewdata(self, request, id=None, name=None):
        context = dict(self.admin_site.each_context(request),)
        context['title'] = f"View {id} "
        context['site_header'] = f"View Page"
        context['site_title'] = f"{id}"
        context['viewobject'] = self.MODEL.objects.all().filter(id=id).get()
        context['list_view'] = self.list_view
        return TemplateResponse(request, 'templateResponse/view.html', context=context)
  
    def googlemap(self, request, id=None, name=None):
            context = dict(self.admin_site.each_context(request),)
            context['title'] = f"Property On Google Map {id} "
            context['site_header'] = f"View Property on map"
            context['site_title'] = f"{id}"
            context['viewobject'] = self.MODEL.objects.all().filter(id=id).get()
            context['list_view'] = self.list_view
            return TemplateResponse(request, 'templateResponse/googlemap.html', context=context)
    
    def gallery(self, request, id=None, name=None):
        context = dict(self.admin_site.each_context(request),)
        context['title'] = f"Media Gallery for {name} "
        context['site_header'] = f"Media"
        context['site_title'] = f"{name} Media Gallery Files"
        context['image_objects'] = PropertyMedia.objects.all().filter(property_id=id)
        context['id'] = str(id)
        return TemplateResponse(request, 'templateResponse/gallery.html', context=context)
   
    def propertymedia(self, request, id=None, name=None):
        context = dict(self.admin_site.each_context(request),)
        context['title'] = f"Add extra media files for {name} "
        context['site_header'] = f"Media"
        context['site_title'] = f"{name} Media Files"
        context['id'] = str(id)
        context['site'] = f"{self.admin_site.name}/{str(self.m).replace('.','/').lower()}"
        context['form'] = PropertyForm()
        
        if request.method == "POST":
            if len(request.FILES) > 0:
                
                for x,y in request.FILES.dict().items():
                    PropertyMedia.objects.create(image=y, property_id=id)

        return TemplateResponse(request, 'templateResponse/addmedia.html', context=context)
        


   
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
client_dashboard_site.register(MatrixProperty, PropertiesAdminsite)



class PropertySalesModelAdmin(admin.ModelAdmin):
    list_display = ADMIN_LIST_DISPLAY_PROPERTYSALESMODEL
    
    list_display_links = ['consultant']
    list_form = '__all__'
    exclude = ['pro_price']
    # list_form = ['first_name','last_name']

    MODEL =  PropertySalesModel
    m = MODEL._meta
    
    template_list = os.path.realpath(f'{CURRENT_MAIN_TEMPLATE}/templates/{CURRENT_TEMPLATE}/{m.app_label}/{m.model_name}/change_list.html')
    template_form = os.path.realpath(f'{CURRENT_MAIN_TEMPLATE}/templates/{CURRENT_TEMPLATE}/{m.app_label}/{m.model_name}/change_form.html')

    delete_confirmation_template = template_list if os.path.exists(template_list) else f'{CURRENT_TEMPLATE}/delete_confirmation_template.html'
    # this will change the  change_list according to apps
    change_list_template = template_list if os.path.exists(template_list) else f'{CURRENT_TEMPLATE}/change_list.html'
    # for change form
    change_form_template = template_form if os.path.exists(template_form) else f'{CURRENT_TEMPLATE}/change_form.html'


    def get_urls(self) -> List[URLResolver]:
        urls = super().get_urls()
        add_urls = [
            path('receipt/<str:id>/', self.receipt, name='receipt'),
        ]
        return add_urls + urls
    
    def receipt(self, request, id=None):
        context = dict(self.admin_site.each_context(request),)
        context['title'] = f"Print Receipt For "
        context['site_header'] = f"Receipt"
        context['site_title'] = f"Receipt"
        context['id'] = str(id)
        context['site'] = f"{self.admin_site.name}/{str(self.m).replace('.','/').lower()}"
    
        return TemplateResponse(request, 'templateResponse/receipt.html', context=context)

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
                        self.list_per_page, self.list_max_show_all, self.list_editable, model_admin=self, 
                        sortable_by=sortable_by, 
                        search_help_text=search_help_text
                    )
        
        opts =  cl.model._meta
        if extra_context is None:
            extra_context = {}
        extra_context['referer'] = request.META.get('HTTP_REFERER')
        extra_context['cl'] = cl
        extra_context['formset'] = formset
        extra_context['opts'] = opts
        extra_context['page_title'] = opts.verbose_name
        
        return super().changelist_view(request, extra_context=extra_context)
    
    def save_model(self, request, obj, form, change):
        property_actual_price =  obj.property.pro_actual_price.amount
            
        # check for quantity
        property_actual_qty =  obj.property.pro_actual_qty
        pro_sales_property_qty =  obj.pro_qty

        if ( (property_actual_qty <= pro_sales_property_qty) ):
            # 
           
            property_price =  int(pro_sales_property_qty) * float(property_actual_price) - float(obj.discount)
            obj.pro_price =  property_price
            balance = float(obj.amountPaid) - float(property_price)
            obj.balance= balance
            return super().save_model(request, obj, form, change)
        else:
            pass
    
client_dashboard_site.register(PropertySalesModel, PropertySalesModelAdmin)
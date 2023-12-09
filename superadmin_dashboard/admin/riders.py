from typing import Any, Dict, Optional
from django.http import HttpResponse
from django.contrib import admin
from django.forms import formset_factory
from django.contrib.admin.views.main import ChangeList
from django.http.request import HttpRequest
import os



from authuser.models import *


from superadmin_dashboard.admin.base_admin import (
    superadmin_dashboard_site,
    CURRENT_MAIN_TEMPLATE,
    CURRENT_TEMPLATE,
    
)

# student/logout/
# student/password_change/
# <form method="post" id="login-form" action="{% url 'admin:login' %}">
# <form method="post" id="login-form" action="{% url 'admin:login' %}?next={{ request.GET.next }}">


MODEL =  Rider


# Register your models here using the student_site
class RiderCustomAdminsite(admin.ModelAdmin):
    list_display = ['fullname']
    list_display_links = ['fullname']
    
    m = MODEL._meta

    template_list = os.path.realpath(f'{CURRENT_MAIN_TEMPLATE}/templates/{CURRENT_TEMPLATE}/{m.app_label}/{m.model_name}/change_list.html')
    template_form = os.path.realpath(f'{CURRENT_MAIN_TEMPLATE}/templates/{CURRENT_TEMPLATE}/{m.app_label}/{m.model_name}/change_form.html')

    delete_confirmation_template = template_list if os.path.exists(template_list) else f'{CURRENT_TEMPLATE}/delete_confirmation_template.html'

    # this will change the  change_list according to  apps
    change_list_template = template_list if os.path.exists(template_list) else f'{CURRENT_TEMPLATE}/change_list.html'
    # for change form
    change_form_template = template_form if os.path.exists(template_form) else f'{CURRENT_TEMPLATE}/change_form.html'


  

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        from django.forms import modelform_factory
        # to import model form
        form = modelform_factory(self.model, fields='__all__', exclude=self.exclude)
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
        extra_context['opts'] = optsform = modelform_factory(self.model, fields='__all__')
        extra_context['page_title'] = opts.verbose_name
        
        return super().changelist_view(request, extra_context=extra_context)


superadmin_dashboard_site.register(MODEL, RiderCustomAdminsite)

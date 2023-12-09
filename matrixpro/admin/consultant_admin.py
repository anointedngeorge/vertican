from django.contrib import admin
from django.urls import path
from django.utils import timezone
from django.http import HttpRequest, HttpResponse
from matrixpro.models.m_consultants import (
    Consultant, ADMIN_LIST_DISPLAY
)

from import_export.admin import ImportExportModelAdmin
from matrixpro.mresources.consultantresource import (
    ConsultantResources
)
import os
import pandas as pd
from tablib import Dataset
from plugins import generator
from plugins.file_reader import (
    csvWriterMultipleRow,reader
)
from actions.exportToDifferentFormat import *
from actions.createAccount import *






@admin.register(Consultant)
class ConsultantAdmin(admin.ModelAdmin):
    list_display = ADMIN_LIST_DISPLAY
    printable_list = ADMIN_LIST_DISPLAY
    list_filter = ['first_name','last_name','phone']
    exclude = [
               'is_active',
               'is_staff',
               'date_joined',
               'last_login',
               'roles',
               'is_superuser',
               'code',
               'username',
               'user_permissions',
               'groups'
            ]
    
    actions = [exportDataCsv, viewDataInPDF, DownloadPDF]

    def response_add(self, request: HttpRequest, obj, post_url_continue: None) -> HttpResponse:
        obj.is_active = True
        obj.is_staff = True
        obj.code = generator(6)
        obj.username = f"{obj.first_name}{generator(6)}"
        return super().response_add(request, obj, post_url_continue)

    def get_urls(self):
        url = super().get_urls()
        new_url = [
             path('export-file/', self.export, name='export-file'),
             path('import-file/', self.import_file, name='import-file'),
        ]
        urls =  new_url + url
        return urls

    
    def export(self, request):
       
        filename =  self.model.__name__
        resources_file = ConsultantResources()
        dataset = resources_file.export()
        response = HttpResponse(dataset.csv, content_type='text/csv')
        f = f"{filename}_{timezone.localdate()}.csv"
        response['Content-Disposition'] = f"attachment; filename='{f}'"
        return response



    def import_file(self, request):
        try:
            resources_file = ConsultantResources()
            if request.method == 'POST':
                data_file_name =  os.path.realpath('templates/data.csv')
                if os.path.exists(data_file_name):
                    importedfile = request.FILES['file'].read().decode('utf-8')
                    d = csvWriterMultipleRow(file_path=data_file_name, data_file=importedfile)
                    # reader the file
                    r_file_data = reader(filepath=data_file_name)
                    for file_data in r_file_data:
                        Variable, Created = self.model.objects.get_or_create(**file_data)
                        # print(Created)
                    return HttpResponse(r_file_data)
                else:
                    return HttpResponse('File does not exist')

        except Exception as e:
            print(e)
            return HttpResponse(f"{e}")
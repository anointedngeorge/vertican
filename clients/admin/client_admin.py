from django.contrib import admin
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from clients.models.m_client import (
    MatrixClient, ADMIN_CLIENT_LIST_DISPLAY
)
from import_export.admin import ImportExportModelAdmin
from django.urls import path
from django.utils import timezone
from django.http import HttpResponse
from plugins.file_reader import (
    csvWriterMultipleRow,reader
)
import os
import uuid
from plugins.generator import generator


@admin.register(MatrixClient)
class ClientAdmin(admin.ModelAdmin):
    list_display = ADMIN_CLIENT_LIST_DISPLAY
    exclude = [
               'is_active',
               'is_staff',
               'date_joined',
               'last_login',
               'roles',
               'is_superuser',
               'code',
               'username',
               'groups',
               'user_permissions'
            ]

    def get_urls(self):
        url = super().get_urls()
        new_url = [
             path('export-file/', self.export, name='export-file'),
             path('import-file/', self.import_file, name='import-file'),
        ]
        urls =  new_url + url
        return urls

    def response_add(self, request: HttpRequest, obj, post_url_continue=None) -> HttpResponse:
        obj.is_active = True
        obj.is_staff = True
        obj.code = generator(6)
        obj.username = f"{obj.first_name}{generator(6)}"
        return super().response_add(request, obj, post_url_continue)
    
    def export(self, request):
        filename =  self.model.__name__
        response = 'das'
        # resources_file = ConsultantResources()
        # dataset = resources_file.export()
        # response = HttpResponse(dataset.csv, content_type='text/csv')
        # f = f"{filename}_{timezone.localdate()}.csv"
        # response['Content-Disposition'] = f"attachment; filename='{f}'"
        return HttpResponse(response)



    def import_file(self, request):
        try:
            if request.method == 'POST':
                data_file_name =  os.path.realpath('templates/data.csv')
                if os.path.exists(data_file_name):
                    importedfile = request.FILES['file'].read().decode('utf-8')
                    d = csvWriterMultipleRow(file_path=data_file_name, data_file=importedfile)
                    # reader the file
                    r_file_data = reader(filepath=data_file_name)
                    for file_data in r_file_data:
                        Variable, Created = self.model.objects.get_or_create(**file_data)
                        print(Created)
                    return HttpResponse(r_file_data)
                else:
                    return HttpResponse('File does not exist')

        except Exception as e:
            print(e)
            return HttpResponse(f"{e}")

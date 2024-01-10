from django.contrib import admin
from matrixpro.models.m_commision import (ProSaleCommision, ADMIN_LIST_DISPLAY)


from django.urls import path
from django.utils import timezone
from django.http import HttpResponse
from plugins.file_reader import (
    csvWriterMultipleRow,reader
)
import os

@admin.register(ProSaleCommision)
class CommissionAdmin(admin.ModelAdmin):
    list_display =  ADMIN_LIST_DISPLAY



    def get_urls(self):
        url = super().get_urls()
        new_url = [
             path('export-file/', self.export, name='export-file'),
             path('import-file/', self.import_file, name='import-file'),
             path('pay-commission/<int:member_id>/', self.pay_commission, name='pay-commission'),
        ]
        urls =  new_url + url
        return urls

    
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
                        # print(Created)
                    return HttpResponse(f"{Variable} - {Created}")
                else:
                    return HttpResponse('File does not exist')

        except Exception as e:
            print(e)
            return HttpResponse(f"{e}")

    def pay_commission(self, request, member_id=None):
        return HttpResponse('Thank u')
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


def currentDateTime():
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d-%m-%Y_%H:%M:%S")
    return dt_string


def exportDataCsv(modeladmin, request, queryset):
    context = {}
    file_format = 'csv'
    app_name = f"{modeladmin.model.__name__}_{currentDateTime()}".lower()
    modeldata = modeladmin.printable_list if modeladmin.printable_list != None else []
    if not len(queryset) > 1:
        seed =  serializers.serialize('python', queryset)
        selected_seed =  seed[0].get('fields')
        for x in modeldata:
            if selected_seed.get(x) != None:
                context[x] = selected_seed.get(x)
            else:
                context[x] = 'empty'

        filename = os.path.realpath(f"templates/data.{file_format}")
        if os.path.exists(filename):
            open_file = open(filename).read()
            # convert to pandas dataframe
            cpd = pd.DataFrame([context])
            cpd.to_csv(filename, index=False, header=True)
            response = HttpResponse(open_file, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="{}.{}"'.format(app_name,file_format)
            return response
        else:
            return HttpResponse('File does not exist')
       
    else:
        return HttpResponse('Error: Multiple row selected. Solution: Select One Data Row.')
exportDataCsv.short_description = "Export Data in CSV"


def viewDataInPDF(modeladmin, request, queryset):
    try:
            app_name = f"{modeladmin.model.__name__}_{currentDateTime()}".lower()
            
            file_format = str('pdf').lower()
            filename = os.path.realpath(f"templates/templateresponse/pdf_profile.html")
            
            context = {}
            app_name = f"{modeladmin.model.__name__}_{currentDateTime()}".lower()
            # convert the modelname printable area to a string
            modeldata = ' '.join(modeladmin.printable_list).replace(' ', ',') if modeladmin.printable_list != None else []
            context['modeldatas'] = modeldata
            context['queryset'] = queryset

            # self.fileFormat(request, file_format, code)
            if os.path.exists(filename):
                template = get_template(filename)
                html  = template.render(context)
                result = BytesIO()
                pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
                if not pdf.err:
                    response = HttpResponse(result.getvalue(), content_type='application/{}'.format(file_format))
                    # response['Content-Disposition'] = 'attachment; filename="{}.{}"'.format(app_name,file_format)
                    result.seek(0)
                    return response
                return None
    except Exception as e:
        return HttpResponse(e)

viewDataInPDF.short_description = "View In PDF"


def DownloadPDF(modeladmin, request, queryset):
    try:
            app_name = f"{modeladmin.model.__name__}_{currentDateTime()}".lower()
            context = {}
            file_format = str('pdf').lower()
            filename = os.path.realpath(f"templates/templateresponse/pdf_profile.html")
            # self.fileFormat(request, file_format, code)
            if os.path.exists(filename):
                template = get_template(filename)
                html  = template.render(context)
                result = BytesIO()
                pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
                if not pdf.err:
                    response = HttpResponse(result.getvalue(), content_type='application/{}'.format(file_format))
                    response['Content-Disposition'] = 'attachment; filename="{}.{}"'.format(app_name,file_format)
                    result.seek(0)
                    return response
                return None
    except Exception as e:
        return HttpResponse(e)

DownloadPDF.short_description = "Download In PDF"
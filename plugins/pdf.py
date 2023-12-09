from django.utils.html import format_html, html_safe
from django.http import FileResponse
from django.template.loader import get_template
from django.shortcuts import render, redirect
from io import BytesIO
# from xhtml2pdf import pisa
from django.http import HttpResponse

def convert_to_file_to_pdf(file_format='pdf', template='', context={}):
    pass
    return HttpResponse('Pdf Loading...')
    # try:
    #     context = context
    #     file_format = str(file_format).lower()
    #     template = get_template(template)
    #     html  = template.render(context)
    #     result = BytesIO()
    #     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    #     if not pdf.err:
    #         response = HttpResponse(result.getvalue(), content_type='application/{}'.format(file_format))
    #         result.seek(0)
    #         return response
    #     return None
    # except:
    #     pass
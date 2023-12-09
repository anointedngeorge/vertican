from django import template
import json
from django.core import serializers
from django.utils import timezone
import datetime as dt
from django.utils.html import format_html
from django.utils.safestring import mark_safe
import itertools

register = template.Library()


def querySet_to_list(qs):
    """
    this will return python list<dict>
    """
    return [dict(q) for q in qs]



@register.simple_tag
def addButton(request=None, id='', title='', url=''):
    res=request.META
    htt = f"{res['wsgi.url_scheme']}://{res['HTTP_HOST']}"
    # <button type="button" class="btn btn-primary" data-toggle="modal" data-target=".bd-example-modal-lg">Large modal</button>
    btn = ''
    btn += f"<button type='button' id='{id}' data-url='{htt}/loadmodal/modal_{url}' class='btn btn-primary btnclass' data-toggle='modal' data-target='.bd-example-modal-lg'>Add {title}</button>"
    return format_html(btn)
# http://127.0.0.1:8000/dashboard/plan



def tableHeadContent(head=[]):
    table = ''
    table += "<thead>"
    table += "<tr>"
    for h in head:
        formt = f"{h}".replace('_', ' ').upper()
        table += f"<td>{formt}</td>"
    table += "</tr>"
    table += "</thead>"
    return table



def tableBodyContent(body=[], head_data=[]):
    table = ''
    table += "<tbody>"
    for b in body:
        bb =  b.get('fields')
        table += "<tr>"
        for h in head_data:
            table += f"<td>{bb.get(h)}</td>"
        table += "</tr>"
        table += "</tbody>"
    return table




@register.simple_tag
def _table(head_data='heading1,heading2,heading3', body_data=[]):
    head_s =  head_data.split(',')
    body_data = serializers.serialize(format='python', queryset=body_data, use_natural_foreign_keys=True, use_natural_primary_keys=True)
    # print(body_data)
    table = ""
    table += "<div class='table-responsive'>"
    table += "<table class='table table-sm styled-table' border=.2>"
    # table += "Hello world"
    table += tableHeadContent(head=head_s)
    table += tableBodyContent(body=body_data, head_data=head_s)
    table += "</table>"
    table += "</div>"
    return format_html(table)
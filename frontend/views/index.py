from django.shortcuts import render
from django.http import HttpResponse

from matrixpro.models.m_property import MatrixProperty

# Create your views here.


FRONTEND_TEMPLATE = 'property'



def index(request, pagename=None, id=None):
    context = {}
    try:
    # context.update(frontendContextProcessor(request))
        if (pagename) and (pagename != 'index') and not (str(pagename).__contains__('.html')):
            context['id'] = id
            return render(request, f'{FRONTEND_TEMPLATE}/{pagename}.html', context=context)
        else:
            context['id'] = id
            return render(request, f'{FRONTEND_TEMPLATE}/index.html', context=context)
    except Exception as e:
        return HttpResponse(str(e))



def property_details(request, id=None):
    context = {}
    try:
        prop = MatrixProperty.objects.all()
        if prop.filter(id=id).exists():
           founddata = prop.filter(id=id).get()
           context['m_property'] = founddata
        return render(request, f'{FRONTEND_TEMPLATE}/property_details.html', context=context)
    except Exception as e:
        return HttpResponse(str(e))

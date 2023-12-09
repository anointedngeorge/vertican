# from django.http import HttpResponse
# from .resources import PersonResource

# def export(request):
#     person_resource = PersonResource()
#     dataset = person_resource.export()
#     response = HttpResponse(dataset.csv, content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="persons.csv"'
#     return response
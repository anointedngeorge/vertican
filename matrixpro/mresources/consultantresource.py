from tablib import Dataset
from import_export import resources

from consultants.models import *


class ConsultantResources(resources.ModelResource):
    
    class Meta:
        model = Consultant
        # fields = ('member')


from django.db import models
from matrixpro.models import *
import time
from django.shortcuts import get_object_or_404
# from matrixpro.models import *
# from clients.models.m_client import MatrixClient
from core.core import CoreBaseModel
from djmoney.models.fields import MoneyField

ADMIN_LIST_DISPLAY_PROPERTYSALESMODEL =  ['action', 'consultant','property','client',
                                          'pro_qty','created_date','status','balance','pro_price']

class PropertySalesModel(CoreBaseModel):
    consultant = models.ForeignKey(to="consultants.Consultant", 
    on_delete=models.CASCADE, null=True, related_name='sales_member_rel')
    property  = models.ForeignKey(to='matrixpro.MatrixProperty', 
    on_delete=models.CASCADE, related_name='property_rel', null=True)

    client  = models.ForeignKey(to='clients.MatrixClient', null=True, on_delete=models.CASCADE, 
                                related_name='client_rel')
    pro_qty  = models.IntegerField(verbose_name='Property qty', default=0 )
    pro_price  = models.FloatField(max_length=500, null=True, blank=True)
    discount = models.FloatField(max_length=300, default=0.00 )
    amountPaid = models.FloatField(max_length=500, null=True, blank=True, default=0.00)
    balance  = models.FloatField(max_length=500, null=True, blank=True, editable=False, default=0.00)
    status  = models.CharField(max_length = 150,blank=True, null=True, 
                               choices=[('unpaid','Unpaid')])
    created_date  = models.DateField(auto_now=True, null=True)
    
    class Meta:
        verbose_name = 'Property Sales'
        verbose_name_plural = 'Property Sales'

    def __str__(self) -> str:
        return f"{self.property}"
    


    def _add_date(self):
        timestamp = int(self.created_date)
        dtime = str(time.strftime("%m %d %Y",time.localtime(timestamp))).replace(" ", "-")
        return dtime

    def action(self):
        from plugins.dropdown import table_dropdown
        data = [
            {"name":"Receipt", "url":f"receipt/{self.id}/", "modal":True},
        ]
        if self.status == 'pending':
            data += [{"name":"unpaid", "url":f"unpaid/{self.id}/"},]
        return table_dropdown(title="Choose", content=data )
    
    
    
    
    
    
    
    

    
    
    
    
    
    
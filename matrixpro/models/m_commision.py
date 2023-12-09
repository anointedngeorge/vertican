from django.db import models
import datetime
import time
from django.utils.html import format_html
from django.urls import reverse_lazy
from core.core import CoreBaseModel


ADMIN_LIST_DISPLAY = ['member', 'sale', 'seller', 'amount','_level','status','_added_date','action']

class ProSaleCommision(CoreBaseModel):
    member = models.ForeignKey(to="consultants.Consultant", 
    on_delete=models.CASCADE, null=True, related_name='sales_member_commision_rel')
    sale = models.ForeignKey(to="matrixpro.PropertySalesModel", 
    on_delete=models.CASCADE, null=True, related_name='sales_sale_commision_rel')
    seller = models.ForeignKey(to="consultants.Consultant", 
    on_delete=models.CASCADE, null=True, related_name='sales_seller_commision_rel')
    amount = models.CharField(max_length = 150)
    level = models.CharField(max_length = 150)
    status = models.CharField(max_length = 150)
    added_date = models.CharField(max_length = 150)

    class Meta:
        verbose_name = 'Commission'
        verbose_name_plural = 'Commissions'

    def __str__(self) -> str:
        return f"{self.member} - {self.amount}"

   
    def _level(self):
        if self.level == str(0):
            return 'Direct'
        return self.level
    
    def _added_date(self):
        timestamp = int(self.added_date)
        dtime = str(time.strftime("%m %d %Y",time.localtime(timestamp))).replace(" ", "-")
        return dtime

    def action(self):
        if self.status == 'unpaid':
            return format_html('<a href="{}" title="Pay" class="btn btn-sm btn-primary">Pay</a>',
                reverse_lazy("admin:pay-commission", args=[
                        self.member_id,
                        ])
            )
        return 'Settled'
    
    
    
from django.db import models
from core.core import CoreBaseModel

class PropSaleInfo(CoreBaseModel):

    pro_title = models.CharField(max_length = 150)
    pro_price = models.CharField(max_length = 150)
    member = models.ForeignKey(to="consultants.Consultant", on_delete=models.CASCADE, 
    related_name='consultant_rel')
    
    qty = models.IntegerField(verbose_name='Quantity')
    location = models.CharField(max_length = 150)
    add_date = models.CharField(max_length = 150)

    class Meta:
        verbose_name = 'Property Sale Info'
        verbose_name_plural = 'Property Sale Info'
    

    def __str__(self) -> str:
        return f"{self.member} - {self.pro_price}"
    
    
    
    
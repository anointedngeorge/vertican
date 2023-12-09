from djmoney.models.fields import MoneyField
from django.db import models
from django.utils import timezone
import datetime
from core.core import CoreBaseModel,CoreBaseModelWithImage
from django.http import HttpResponse
from choices import *
from ckeditor.fields import RichTextField


class MatrixPropertyStatus(CoreBaseModel):
    shortname  = models.CharField(max_length=250, blank=True, null=True)
    name  = models.CharField(max_length=250)
    index = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Property Status'
        verbose_name_plural = 'Property Status'

    def __str__(self) -> str:
        return str(self.name)


class MatrixPropertyType(CoreBaseModel):
    name  = models.CharField(max_length=250)
    short_description  = models.CharField(max_length=250, null=True)
    index = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name = 'Property Type'
        verbose_name_plural = 'Property Types'



class MatrixPropertyFeatures(CoreBaseModel):
    name  = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Property Feature'
        verbose_name_plural = 'Property Feature'

    def __str__(self) -> str:
        return str(self.name)



LIST_MatrixProperty = ['status','property_title','property_desc','property_location','property_address', 'property_type',
            'pro_actual_price','pro_actual_qty','pro_actual_price'       
            ]


LIST_MatrixProperty_view = 'status,property_title,property_desc,property_location,property_address,property_type, pro_actual_price,pro_actual_qty,pro_actual_price'
            
class MatrixProperty(CoreBaseModelWithImage):
    property_title = models.CharField(blank=True,null=True,max_length = 150)
    property_desc = RichTextField( verbose_name='Property Descriptions', null=True )
    property_location = models.CharField(blank=True,null=True,max_length = 150)
    property_address = models.CharField(blank=True,null=True,max_length = 150)
    property_type = models.ForeignKey("matrixpro.MatrixPropertyType", on_delete=models.CASCADE)
    pro_actual_price = MoneyField(max_digits=30, decimal_places=2, default_currency='NG', null=True)
    pro_actual_qty  = models.IntegerField(default=0, verbose_name='Property Actual qty')
    
    property_size = models.CharField(blank=True,null=True,max_length = 150)
    promo_code = models.CharField(blank=True,null=True,max_length = 150)
    
    promo_price = MoneyField(max_digits=30, 
                            decimal_places=2, 
                            default_currency='NG',
                            null=True, blank=True
                        )
    

    promo_duration = models.DateField(auto_now=False, null=True, blank=True)

    payment_terms = models.CharField(blank=True,null=True,max_length = 150)
    property_state = models.CharField(max_length=150, choices=PropertyStatusChoice.choices, 
                                      default=PropertyStatusChoice.NEW)
    status = models.ForeignKey("matrixpro.MatrixPropertyStatus", on_delete=models.CASCADE, null=True)
   
    active = models.CharField(null=True,choices=[('yes','Yes'), ('no','No')], max_length=100)
    is_frontend = models.CharField(null=True,choices=[('yes','Yes'), ('no','No')], max_length=100)
    posted_by = models.ForeignKey("consultants.Consultant", on_delete=models.CASCADE, blank=True, null=True)
    property_features = models.ManyToManyField("matrixpro.MatrixPropertyFeatures", blank=True)


    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self) -> str:
        return f"{self.property_title}, Price ({self.pro_actual_price}), (Location: {self.property_location})"
    
    # def date_field(self):
    #     date = datetime.datetime.fromtimestamp(int(self.add_date))
    #     formatted_date = date.strftime("%B %d, %Y")
    #     return formatted_date

    def action(self):
        from plugins.dropdown import table_dropdown
        data = [
            {"name":"View", "url":f"viewdata/{self.id}/", "modal":True},
            {"name":"Google Map", "url":f"googlemap/{self.id}/"},
            {"name":"Add Media", "url":f"propertymedia/{self.id}/{self.property_title}/"},
            {"name":"Gallery", "url":f"gallery/{self.id}/{self.property_title}/", "modal":True},
        ]
        return table_dropdown(title="Choose", content=data )
    


def ImageValidator(value):
    import os
    from django.core.exceptions import ValidationError
    from PIL import Image

    # Get the file extension
    ext = os.path.splitext(value.name)[1].lower()

    # Check if the file extension is not an image format
    if ext not in ['.jpg', '.jpeg', '.png']:
        raise ValidationError('Only image files (jpg, jpeg, png, gif) are allowed.')

    # You can also check the image content to ensure it's a valid image
    try:
        with Image.open(value) as img:
            img.verify()
    except Exception:
        raise ValidationError('Invalid image file.')


class PropertyMedia(CoreBaseModel):
    image = models.ImageField(upload_to='images/', validators=[ImageValidator])
    property =  models.ForeignKey("matrixpro.MatrixProperty", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Property Media'
        verbose_name_plural = 'Property Media'
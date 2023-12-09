from django.db import models


class SliderActiveChoice(models.IntegerChoices):
    ISACTIVE = 1, "Is Active"
    NOTACTIVE = 0, "Not Active"


class SliderShowOnlineChoice(models.IntegerChoices):
    SHOW = 1, "Show Slider"
    DONT_SHOW = 0, "Don't Show Slider"




class PropertyStatusChoice(models.TextChoices):
    NEW = "new", "New"
    OUTOFSTOCK = "outofstock", "Out Of Stock"
    RENT = "rent", "For Rent"
    SALE = "sale", "For Sale"
from django.db import models

class AdminClass(models.Model):
    member_id = models.CharField(max_length = 150)

    class Meta:
       
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'
    
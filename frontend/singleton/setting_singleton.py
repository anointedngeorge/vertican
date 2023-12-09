from django.db import models

class SettingSingletonModel(models.Model):
    tel = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=300, null=True, blank=True)
    site_title = models.CharField(max_length=255, null=True, blank=True)
    site_logo = models.ImageField(upload_to="setting", null=True, blank=True)
    site_subtitle = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    description_title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True, blank=True)
    aboutus = models.TextField(null=True, blank=True)
    footer_section = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    youtube = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True

class SettingSingletonModelManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset()
        if queryset.exists():
            return queryset
        return []


class SettingSingletonModelMixin(models.Model):
    objects = SettingSingletonModelManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1  # Set a fixed primary key value to ensure only one record exists
        super().save(*args, **kwargs)

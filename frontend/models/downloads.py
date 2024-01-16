from django.db import models


class Downloads(models.Model):
    name = models.CharField(max_length=150)
    # logo = models.CharField(max_length=150, null=True, blank=True)
    logo = models.ForeignKey("frontend.FrontendImage", on_delete=models.PROTECT, null=True)
    # logo = models.ImageField(upload_to='contact', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Downloads"
    
    


class DownloadContent(models.Model):
    download = models.ForeignKey("frontend.Downloads", on_delete=models.CASCADE, related_name="downloads" )
    title = models.CharField(max_length=150, null=True, blank=True)
    link = models.URLField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title


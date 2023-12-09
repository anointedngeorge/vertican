# from bidxx.admin import admin, site
# from baton.autodiscover import admin
from django.contrib import admin
from django.urls import re_path as url
from django.views.static import serve
from django.conf import settings
from django.urls import path, include
from django.conf import settings

# admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    
    url(r'^media/(?P<path>.*)$', serve,  {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]


from clientdashboard.admin import client_dashboard_site
# clients
urlpatterns += [
    path('client/', client_dashboard_site.urls, name='client'),
]
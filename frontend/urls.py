# from bidxx.admin import admin, site
# from baton.autodiscover import admin
from django.contrib import admin
from django.urls import re_path as url
from django.views.static import serve
from django.conf import settings
from django.urls import path, include
from django.conf import settings
from frontend import views
# admin.autodiscover()

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:pagename>', views.index, name='index'),
    path('property_detail/<uuid:id>/', views.property_details, name='property_detail'),
]


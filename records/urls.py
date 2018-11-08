from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$', views.record_create, name="create"),
    url(r'^$', views.records, name="records"),
]

from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.records, name="records"),
    url(r'^create$', views.record_create, name="create"),
]

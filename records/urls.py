from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$', views.record_create, name="create"),
    url(r'^$', views.records, name="records"),
    url(r'^addpet/$', views.add_pet, name="addpet"),
    url(r'^pets/$', views.your_pet, name="yourPet"),
    url(r'^your-pet/$', views.your_pet, name="yourPet"),
    url(r'^stats/$', views.stats, name="stats"),
]

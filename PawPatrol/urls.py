from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    #path('admin/', admin.site.urls),
    #is the same as:
    url(r'^admin/', admin.site.urls, name="admin"),
    # include means that Django must include record
    # app's URLs.py file too.
    url(r'^records/', include('records.urls')),
    url(r'^about/$', views.about, name="about"),
    url(r'^$', views.homepage, name="main_home"),

]

urlpatterns += staticfiles_urlpatterns()

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('admin/', admin.site.urls),
    #is the same as:
    url(r'^admin/', admin.site.urls, name="admin"),
    # include means that Django must include record
    # app's URLs.py file too.
    url(r'^records/', include('records.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^stats/', include('stats.urls')),
    url(r'^about/$', views.about, name="about"),
    url(r'^your-pet/$', views.your_pet, name="your-pet"),
    url(r'^$', views.homepage, name="main_home"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

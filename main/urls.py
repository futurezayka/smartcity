from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from main.views import *
from smartcity.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('', index, name='home')
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

from django.conf.urls import url
from . import views

# here we have to import our url


urlpatterns = [
    url(r'^$', views.home),
    url(r'^about/$', views.about),
    url(r'^json/$', views.json_data),
]

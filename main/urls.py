from django.conf.urls import url
from . import views

# here we have to import our url


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about,name='about'),
    url(r'^json/$', views.json_data,name='json'),
    url(r'^panel/$',views.panel, name='panel'),
]

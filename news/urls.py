from django.conf.urls import url
from . import views

urlpatterns = [
    # we can use w+
    url(r'^news/(?P<word>.*)/$', views.news_detail, name='news_detail'),
]

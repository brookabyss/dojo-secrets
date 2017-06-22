from django.conf.urls import url
from . import views1
urlpatterns = [
    url(r'^$', views1.index),
    url(r'^register$', views1.register),
    url(r'^login$', views1.login),
]

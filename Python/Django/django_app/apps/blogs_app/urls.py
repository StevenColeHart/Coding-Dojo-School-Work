from django.conf.urls import url
from . import views   


urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^edit$', views.edit),
    ]
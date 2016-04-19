from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create$', views.point_create, name='point_create'),
    url(r'^$', views.point_list, name='point_list'),
]

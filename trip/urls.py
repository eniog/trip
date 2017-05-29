from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.trip_list, name='trip_list'),
    url(r'^trip/(?P<pk>[0-9]+)/$', views.trip_detail, name='trip_detail'),
]

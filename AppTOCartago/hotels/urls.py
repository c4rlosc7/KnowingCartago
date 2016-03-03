#url configuracion interna

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^hotels/', views.hotels),
    url(r'^hotel/(?P<pk>[0-9]+)/$', views.hotel_detail)
]

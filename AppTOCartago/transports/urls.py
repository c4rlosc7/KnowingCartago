#url settings of transports

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^transports/', views.transports),
	url(r'^transport/(?P<pk>[0-9]+)/$', views.transport_detail)
]


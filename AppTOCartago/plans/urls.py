#url settings of plans

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^plans/', views.plans),
	url(r'^plan/(?P<pk>[0-9]+)/$', views.plan_detail)
]


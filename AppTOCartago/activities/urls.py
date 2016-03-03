#url settings of activities

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^activities/', views.activities),
	url(r'^activity/(?P<pk>[0-9]+)/$', views.activities_detail)
]


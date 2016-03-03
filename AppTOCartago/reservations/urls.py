#url configuracion interna

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^reservations/', views.reservations)
]


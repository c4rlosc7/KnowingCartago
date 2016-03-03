
from django.http import HttpResponse

from django.template import loader

from .models import Hotel

from django.shortcuts import render, get_object_or_404


# Pagina inicio
def home(request):
	template = loader.get_template('index.html')
	context = {}
	return HttpResponse(template.render(context, request))

#Hoteles
def hotels(request):	
	hotel = Hotel.objects.order_by('id')
	template = loader.get_template('hotels.html')
	context = {
		'hotel': hotel
	}
	return HttpResponse(template.render(context, request))

#Hotel Detallado
def hotel_detail(request, pk):
	hotel = get_object_or_404(Hotel, pk=pk)
	template = loader.get_template('hotel_detail.html')
	context = {
		'hotel': hotel
	}	
	return HttpResponse(template.render(context, request))





from django.http import HttpResponse

from django.template import loader

from .models import Transport

from django.shortcuts import render, get_object_or_404
# Create your views here.

# Transports
def transports(request):
	transport = Transport.objects.order_by('id')
	template = loader.get_template('transports.html')
	context = {
		'transport': transport
	}
	return HttpResponse(template.render(context, request))

#Transport Detail
def transport_detail(request, pk):
	transport = get_object_or_404(Transport, pk=pk)
	template = loader.get_template('transport_detail.html')
	context = {
		'transport': transport
	}	
	return HttpResponse(template.render(context, request))
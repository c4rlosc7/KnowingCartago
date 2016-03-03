
from django.http import HttpResponse

from django.template import loader

from .models import Plan

from django.shortcuts import render, get_object_or_404

# Create your views here.

# Plans
def plans(request):
	plan = Plan.objects.order_by('id')
	template = loader.get_template('plans.html')
	context = {
		'plan': plan
	}
	return HttpResponse(template.render(context, request))

#Plans detail
def plan_detail(request, pk):
	plan = get_object_or_404(Plan, pk=pk)
	template = loader.get_template('plan_detail.html')
	context = {
		'plan': plan
	}	
	return HttpResponse(template.render(context, request))	
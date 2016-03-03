
from django.http import HttpResponse

from django.template import loader

from .models import Activity

from django.shortcuts import render, get_object_or_404
# Create your views here.

#Activities
def activities(request):	
	activity = Activity.objects.order_by('id')
	template = loader.get_template('activities.html')
	context = {
		'activity': activity
	}
	return HttpResponse(template.render(context, request))

#Activities Detail
def activities_detail(request, pk):
	activity = get_object_or_404(Activity, pk=pk)
	template = loader.get_template('activity_detail.html')
	context = {
		'activity': activity
	}	
	return HttpResponse(template.render(context, request))

	
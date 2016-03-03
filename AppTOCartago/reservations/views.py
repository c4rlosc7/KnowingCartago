
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import Reservation
from .forms import ReservationForm
from django.shortcuts import render, get_object_or_404

# Create your views here.

def reservations(request):
	if request.method == 'POST':
		form = ReservationForm(request.POST)
		if form.is_valid():
			reservation = form.save()
			reservation.save()
			return HttpResponseRedirect('/')
	else:
		form = ReservationForm()

	template = loader.get_template('reservations.html')
	context = {
		'form': form
	}
	return HttpResponse(template.render(context, request))
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import Contact
from .forms import ContactForm
from django.shortcuts import render, get_object_or_404

# Create your views here.

# Contacto
#def contacts(request):
#	template = loader.get_template('contacts.html')
#	context = {}
#	return HttpResponse(template.render(context, request))

def new_contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			contact = form.save()
			contact.save()
			return HttpResponseRedirect('/')
	else:
		form = ContactForm()

	template = loader.get_template('contacts.html')
	context = {
		'form': form
	}
	return HttpResponse(template.render(context, request))
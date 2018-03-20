from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from mysite.contact.forms import ContactForm

@csrf_exempt

def contact(request):
	errors = []
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email','noreply@example.com'),
				['liyongchun@mysite.com'],
					)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(
				initial = {'subject':'I love your site!'}
				)
	return render_to_response('contact_form.html',{'form':form})

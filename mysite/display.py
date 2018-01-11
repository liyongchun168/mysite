from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def display(request):
	values = request.META.items()
	values.sort()
	t = get_template('display.html')
	html = t.render(Context({'values':values}))
	return HttpResponse(html)

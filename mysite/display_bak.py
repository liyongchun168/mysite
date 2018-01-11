from django.http import HttpResponse

def display(request):
	values = request.META.items()
	values.sort()
	html = []
	for k,v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k,v))
	return HttpResponse('<table><tr><th>Items</th><th>Contents</th></tr>%s</table>' % '\n'.join(html))

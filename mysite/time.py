from django.shortcuts import render_to_response
import datetime

def current_datetime(request):
	n = datetime.datetime.now()
	return render_to_response('current_datetime.html',{'current_date':n})

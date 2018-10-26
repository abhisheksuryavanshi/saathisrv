from django.http import HttpResponse
from django.template import loader
from .models import camp

def index(request):
	all_camps = camp.objects.all()
	template = loader.get_template('paratha/listall.html')
	context = {'all_camps' : all_camps}
	return HttpResponse(template.render(context, request))
from django.http import HttpResponse
from django.template import loader
from .models import camp
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import campSerializer
import json

def index(request):
	all_camps = camp.objects.all()
	template = loader.get_template('paratha/listall.html')
	context = {'all_camps' : all_camps}
	return HttpResponse(template.render(context, request))

class camplist(APIView):

	def get(self, request):
		all_camps = camp.objects.all()
		ser = campSerializer(all_camps, many= True)
		e = {"a": {'1,2,352'}, "b": {'4,5,6'}}
		return Response(e)

	def post(self):
		pass
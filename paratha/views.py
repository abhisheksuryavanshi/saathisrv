from django.http import HttpResponse
from django.template import loader
from .models import camp
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import campSerializer
import json
import requests
from rest_framework.decorators import api_view
import math 

def index(request):
	all_camps = camp.objects.all()
	template = loader.get_template('paratha/listall.html')
	context = {'all_camps' : all_camps}
	return HttpResponse(template.render(context, request))
import codecs

reader = codecs.getreader("utf-8")

def calculate(ax, ay, bx, by):
	ans = (ax - bx)*(ax - bx) + (ay - by)*(ay - by)
	t = math.sqrt(ans)
	return t


class camplist(APIView):
	def get(self, request):
		all_camps = camp.objects.all()
		ser = campSerializer(all_camps, many= True)
		e = {"a": {'1,2,352'}, "b": {'4,5,6'}}
		return Response(e)

	def post(self,request):
		# xcoor = request.POST.get('xcor')
		# ycoor = request.POST.get('ycor')
		from .models import camp
		xcoor = "4"
		xcoor = int(round(float(request.POST.get("xcor"))))
		ycoor = "f"
		ycoor = int(round(float(request.POST.get("ycor"))))

		all_camps = camp.objects.all()

		res = {}

		for camp in all_camps:
			b = calculate(camp.xcor, camp.ycor, xcoor, ycoor)
			
			if(b < 100):
				res[camp.name] = {camp.xcor, camp.ycor}
			print(b)

		# if 'er' in request.POST:
		# 	xcoor += "a"
		# 	xcoor = request.POST.get('ycor')
		# else:
		# 	xcoor += "b"
		# 	xcoor = "iui"

		f = {"x" : xcoor, "y" : ycoor}
		return Response(res)

# def camplist(request, format=None):
# 	if request.method == "POST":
# 		pass
# 	else:
# 		all_camps = camp.objects.all()
# 		ser = campSerializer(all_camps, many= True)
# 		e = {"a": {'1,2,352'}, "b": {'4,5,6'}}
# 		return Response(e, template_name='articles.html')
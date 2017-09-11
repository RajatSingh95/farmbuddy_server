from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Farmer
from django.core import serializers
# Create your views here.
def index(request):
	return HttpResponse('<h1> This is the RestApi. </h1>')

def farmerdetail(request):
	if request.method == 'POST':
		username = request.POST.get('username', None)
		data = { 'farmer_detail': serializers.serialize('json', Farmer.objects.all()) }
		res = JsonResponse(data)
		res['Access-Control-Allow-Origin']="*"
		print(res)
		return res
	

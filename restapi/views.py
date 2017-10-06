from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from django.core import serializers
# Create your views here.
def index(request):
	return HttpResponse('<h1> This is the RestApi. </h1>')

def farmerdetail(request):
	if request.method == 'POST':
		username = request.POST.get('username', None)
		data = { 'farmer_detail': serializers.serialize('json', Farmer.objects.all()  ) }
		res = JsonResponse(data)
		res['Access-Control-Allow-Origin']="*"
		print(res)
		return res

def mapdetail(request):
	if request.method == 'POST':
		username = request.POST.get('username', None)
		data = { 'farmer_detail': serializers.serialize('geojson', Farms.objects.all(),geometry_field='plot') }
		res = JsonResponse(data)
		res['Access-Control-Allow-Origin']="*"
		print(res)
		return res
def housedetail(request):
	if request.method == 'POST':
		username = request.POST.get('username', None)
		data = { 'farmer_detail': serializers.serialize('geojson', Houses.objects.all(),geometry_field='point') }
		res = JsonResponse(data)
		res['Access-Control-Allow-Origin']="*"
		print(res)
		return res 

def cropdetail(request):
	if request.method == 'POST':
		farmid = request.POST.get('farm_id', None)
		data = { 'cropd_detail': serializers.serialize('json', Crops.objects.filter(FID=farmid)) }
		res = JsonResponse(data)
		res['Access-Control-Allow-Origin']="*"
		print(res)
		return res 

def logindetail(request):
	if request.method == 'POST':
		username = request.POST.get('username', None)
		passw = request.POST.get('pswd', None)
		result=Landlord.objects.filter(mobile_no=username, password=passw)
		if result:
			data = { 'login':'success' ,'landlord_detail': serializers.serialize('json', result ) }
		else :
			data={'login': 'failed'}
		res = JsonResponse(data)
		res['Access-Control-Allow-Origin']="*"
		print(res)
		return res	


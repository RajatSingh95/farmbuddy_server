from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from django.core import serializers
# Create your views here.
def index(request):
	return HttpResponse('<h1> This is the RestApi. </h1>')


# It respond to the request for Farmers Data in Json Format.

def farmerdetail(request):
	if request.method == 'POST':
		username = request.POST.get('username', None)
		data = { 'farmer_detail': serializers.serialize('json', Farmer.objects.all()  ) }
		res = JsonResponse(data)
		res['Access-Control-Allow-Origin']="*"
		print(res)
		return res

# It respond to the request for Farms Data with co-ordinates of the polygon in GeoJson Format.
def mapdetail(request):
	if request.method == 'POST':
		username = request.POST.get('username', None)
		data = { 'farmer_detail': serializers.serialize('geojson', Farms.objects.all(),geometry_field='plot') }
		res = JsonResponse(data)
		res['Access-Control-Allow-Origin']="*"
		print(res)
		return res

# It respond to the request for Houses Data of farmer as well as landlord with pinpoint location of houses in GeoJson Format.
def housedetail(request):
	if request.method == 'POST':
		username = request.POST.get('username', None)
		data = { 'farmer_detail': serializers.serialize('geojson', Houses.objects.all(),geometry_field='point') }
		res = JsonResponse(data)
		res['Access-Control-Allow-Origin']="*"
		print(res)
		return res

# It respond to the request for Wells Data associated with the farms with pinpoint location in GeoJson Format. 

def welldetail(request):
	if request.method == 'POST':
		username = request.POST.get('username', None)
		data = { 'well_detail': serializers.serialize('geojson', Wells.objects.all(),geometry_field='point') }
		res = JsonResponse(data)
		res['Access-Control-Allow-Origin']="*"
		print(res)
		return res

# It respond to the request for Crop Data of the farm in Json Format.

def cropdetail(request):
	if request.method == 'POST':
		farmid = request.POST.get('farm_id', None)
		data = { 'crops_detail': serializers.serialize('json', Crops.objects.filter(FID=farmid)) }
		res = JsonResponse(data)
		res['Access-Control-Allow-Origin']="*"
		print(res)
		return res 

# # It respond to the request for Authentication and return Data in case of successfull in Json Format.
def logindetail(request):
	if request.method == 'POST':
		username = request.POST.get('mobile', None)
		password = request.POST.get('pass', None)
		print(username,password)
		result=Landlord.objects.filter(mobile_no=username, password=password)
		if result:
			data = { 'login':'success' ,'landlord_detail': serializers.serialize('json', result ) }
		else :
			data={'login': 'failed'}
		res = JsonResponse(data)
		res['Access-Control-Allow-Origin']="*"
		print(res)
		return res	

def statistic(request):
	if request.method == 'POST':
		ctype = request.POST.get('type', None)
		if ctype=="Rice":
			result=Crops.objects.filter(Name=ctype)
			data = { 'crop_detail': serializers.serialize('json', result ) }
			res = JsonResponse(data)
			res['Access-Control-Allow-Origin']="*"
			print(res)
			return res

		if ctype=="Wells":
			result=Wells.objects.all()
			data = { 'well_detail': serializers.serialize('json', result ) }
			res = JsonResponse(data)
			res['Access-Control-Allow-Origin']="*"
			print(res)
			return res
		if ctype=="Income":
			result=Houses.objects.all()
			data = { 'house_detail': serializers.serialize('json', result ) }
			res = JsonResponse(data)
			res['Access-Control-Allow-Origin']="*"
			print(res)
			return res
		if ctype=="Family":
			result=Houses.objects.all()
			data = { 'family_detail': serializers.serialize('json', result ) }
			res = JsonResponse(data)
			res['Access-Control-Allow-Origin']="*"
			print(res)
			return res


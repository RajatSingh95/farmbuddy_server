from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
import datetime

# Create your models here.
class Houses(models.Model):
	HID=models.AutoField(primary_key=True,null=True)
	point=models.PointField(default=Point(1,1),null=True)

class Farms(models.Model):
	FID=models.AutoField(primary_key=True,null=True)
	plot=models.PolygonField(srid=4326,geography=True)
	area=models.FloatField(default=0.0)
	
	def save(self):
		temp=self.plot.transform(27700,clone=True)
		self.area=temp.area
		super().save(self)
	
class Farmer(models.Model):
	HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE)
	name = models.CharField(max_length=250)
	dob = models.DateField(max_length=250)
	address = models.CharField(max_length=550)
	mobile_no = models.CharField(max_length=250)
	password = models.CharField(max_length=250)

class Landlord(models.Model):
	HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE)
	FID=models.ForeignKey(Farms,to_field='FID',on_delete=models.CASCADE)
	name = models.CharField(max_length=250)
	dob = models.DateField(max_length=250)
	address = models.CharField(max_length=550)
	mobile_no = models.CharField(max_length=250)
	password = models.CharField(max_length=250)

class Advertisement(models.Model):
	landlord_id = models.IntegerField()
	land_price = models.BigIntegerField()
	leased_to = models.IntegerField() #farmer_id
	bid_id = models.IntegerField() #bid given to the particular land

class Bid(models.Model):
	price = models.BigIntegerField()
	farmer_id = models.IntegerField()
	advertisement_id = models.IntegerField()




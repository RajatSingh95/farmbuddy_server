from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
import datetime

# Create your models here.
class Houses(models.Model):
	HID=models.AutoField(primary_key=True)
	point=models.PointField(default=Point(1,1),null=True)
	file=models.FileField(upload_to = 'images/houses/',null=True)
	Members=models.IntegerField(null=True)
	Income=models.IntegerField(null=True)
	def __str__(self):
		return "House : %s" %(self.HID)


class Farms(models.Model):
	FID=models.AutoField(primary_key=True)
	plot=models.PolygonField(srid=4326,geography=True)
	area=models.FloatField(default=0.0)
	file=models.FileField(upload_to = 'images/farms/',null=True)
	def __str__(self):
		return "%s : %s" %(self.FID,self.area)
	
	def save(self):
		temp=self.plot.transform(27700,clone=True)
		self.area=temp.area
		super().save(self)
class Wells(models.Model):
	WID=models.AutoField(primary_key=True)
	HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE)
	point=models.PointField(default=Point(1,1),null=True)
	depth=models.FloatField(default=0.0)
	file=models.FileField(upload_to = 'images/wells/',null=True)
	def __str__(self):
		return "%s : %s" %(self.WID,self.depth)

class Crops(models.Model):
	Name=models.CharField(max_length=50,default="Rice")
	FID=models.ForeignKey(Farms,to_field='FID',on_delete=models.CASCADE)
	Year=models.IntegerField()
	seasons=(('S',"Summer"),('W',"Winter"),('M',"Monsoon"))
	Seasons=models.CharField(max_length=20,choices=seasons)
	Yield=models.FloatField(default=0.0,null=True)
	def __str__(self):
		return "%s : %s" %(self.Name,self.Seasons)
	
class Farmer(models.Model):
	HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE)
	name = models.CharField(max_length=250)
	dob = models.DateField(max_length=250)
	address = models.CharField(max_length=550)
	mobile_no = models.CharField(max_length=250)
	password = models.CharField(max_length=250)
	def __str__(self):
		return "%s : %s" %(self.HID,self.name)

class Landlord(models.Model):
	HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE)
	FID=models.ForeignKey(Farms,to_field='FID',on_delete=models.CASCADE)
	name = models.CharField(max_length=250)
	dob = models.DateField(max_length=250)
	address = models.CharField(max_length=550)
	mobile_no = models.CharField(max_length=250)
	password = models.CharField(max_length=250)
	def __str__(self):
		return "Landlord %s : %s" %(self.FID,self.name)

class Advertisement(models.Model):
	landlord_id = models.IntegerField()
	land_price = models.BigIntegerField()
	leased_to = models.IntegerField() #farmer_id
	bid_id = models.IntegerField() #bid given to the particular land
	def __str__(self):
		return "%s : %s" %(self.landlord_id,self.leased_to)

class Bid(models.Model):
	price = models.BigIntegerField()
	farmer_id = models.IntegerField()
	advertisement_id = models.IntegerField()
	def __str__(self):
		return "%s : %s" %(self.advertisement_id,self.price)

class Yields(models.Model):
	WID=models.ForeignKey(Wells,to_field='WID',on_delete=models.CASCADE)
	Yield=models.FloatField(default=0.0)
	measured_date=models.DateField(default=datetime.date.today)
	def __str__(self):
		return "%s : %s" %(self.WID,self.Yield)



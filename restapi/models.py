from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
import datetime

# Create your models here.

# House Table with columns as follows:
#	1.House Id  2.Pinpoint location of House  3.File/Image related to house. 4. No. of members  5.Annual family income

class Houses(models.Model):
	HID=models.AutoField(primary_key=True)
	point=models.PointField(default=Point(1,1),null=True)
	file=models.FileField(upload_to = 'images/houses/',null=True)
	Members=models.IntegerField(null=True)
	Income=models.IntegerField(null=True)
	def __str__(self):
		return "House : %s" %(self.HID)

# Farm Table with columns as follows:
#	1.Farm Id  2.Lat,Lng of te vertices of farm  3.Area of farm  4.Image

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


# Wells Table with columns as follows:
#	1.Well Id  2.House Id of house having that well  3.Pinpoint location of well  4.Depth of Well  5.Average Yield of the well  6.Image of the well 

class Wells(models.Model):
	WID=models.AutoField(primary_key=True)
	HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE)
	point=models.PointField(default=Point(1,1),null=True)
	depth=models.FloatField(default=0.0)
	Yield=models.FloatField(default=0.0,null=True)
	Area=models.CharField(max_length=100,null=True)
	file=models.FileField(upload_to = 'images/wells/',null=True)
	def __str__(self):
		return "%s : %s" %(self.WID,self.depth)

# Crops Table with columns as follows:
#	1.Crop Name  2.Farm Id where the crop was grown  3.Year  4.Season  5.Average Yield of the the crop in paricular year

class Crops(models.Model):
	Name=models.CharField(max_length=50,default="Rice")
	FID=models.ForeignKey(Farms,to_field='FID',on_delete=models.CASCADE)
	Year=models.IntegerField()
	seasons=(('S',"Summer"),('W',"Winter"),('M',"Monsoon"))
	Seasons=models.CharField(max_length=20,choices=seasons)
	Yield=models.FloatField(default=0.0,null=True)
	def __str__(self):
		return "%s : %s" %(self.Name,self.Seasons)


# Farmer Table with columns as follows:
#	1.House Id  2.Name of the farmer  3.Date of Birth  4.Address  5.Mobile No. 5.Password

	
class Farmer(models.Model):
	HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE)
	name = models.CharField(max_length=250)
	dob = models.DateField(max_length=250)
	address = models.CharField(max_length=550)
	mobile_no = models.CharField(max_length=250)
	password = models.CharField(max_length=250)
	def __str__(self):
		return "%s : %s" %(self.HID,self.name)

# Landlord Table with columns as follows:
#	1.House Id  2.Id of the Farm belonging to that person 3.Name  4.Date of Birth  5.Address 6.Mobile No. 7. Password


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


# Avertisement Table with columns as follows:
#	1.landlord_id who is posting the advertisement  2.land_price  3.leased_to is id of the farmer who won the bid   4.bid_id


class Advertisement(models.Model):
	landlord_id = models.IntegerField()
	land_price = models.BigIntegerField()
	leased_to = models.IntegerField() #farmer_id
	bid_id = models.IntegerField() #bid given to the particular land
	def __str__(self):
		return "%s : %s" %(self.landlord_id,self.leased_to)

# Bid Table with columns as follows:
#	1.Bid set by the farmer(Rs.)  2.Id of Farmer who is bidding  3.Advertisement Id


class Bid(models.Model):
	price = models.BigIntegerField()
	farmer_id = models.IntegerField()
	advertisement_id = models.IntegerField()
	def __str__(self):
		return "%s : %s" %(self.advertisement_id,self.price)

# Yield Table with columns as follows:
#	1.Well Id  2.Yield  3.Date at yield was measured



class Yields(models.Model):
	WID=models.ForeignKey(Wells,to_field='WID',on_delete=models.CASCADE)
	Yield=models.FloatField(default=0.0)
	measured_date=models.DateField(default=datetime.date.today)
	def __str__(self):
		return "%s : %s" %(self.WID,self.Yield)



from django.db import models

# Create your models here.
class Farmer(models.Model):
	name = models.CharField(max_length=250)
	dob = models.DateField(max_length=250)
	address = models.CharField(max_length=550)
	mobile_no = models.CharField(max_length=250)
	password = models.CharField(max_length=250)

class Landlord(models.Model):
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



from django.contrib import admin
from .models import Farmer,Landlord,Bid,Advertisement


# Register your models here.
admin.site.register(Farmer)
admin.site.register(Landlord)
admin.site.register(Advertisement)
admin.site.register(Bid)


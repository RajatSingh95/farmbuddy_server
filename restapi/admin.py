from django.contrib.gis import admin
from .models import *


# Register your models here.
admin.site.register(Farms,admin.OSMGeoAdmin)
admin.site.register(Houses,admin.OSMGeoAdmin)
admin.site.register(Farmer,admin.OSMGeoAdmin)
admin.site.register(Landlord,admin.OSMGeoAdmin)
admin.site.register(Advertisement,admin.OSMGeoAdmin)
admin.site.register(Bid,admin.OSMGeoAdmin)
admin.site.register(Crops,admin.OSMGeoAdmin)
admin.site.register(Wells,admin.OSMGeoAdmin)
admin.site.register(Yields,admin.OSMGeoAdmin)

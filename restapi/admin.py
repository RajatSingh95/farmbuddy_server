from django.contrib.gis import admin
from .models import *


# Register your models here.
admin.site.register(Farms,admin.GeoModelAdmin)
admin.site.register(Houses,admin.GeoModelAdmin)
admin.site.register(Farmer,admin.GeoModelAdmin)
admin.site.register(Landlord,admin.GeoModelAdmin)
admin.site.register(Advertisement,admin.GeoModelAdmin)
admin.site.register(Bid,admin.GeoModelAdmin)
admin.site.register(Crops,admin.GeoModelAdmin)
admin.site.register(Wells,admin.GeoModelAdmin)
admin.site.register(Yields,admin.GeoModelAdmin)

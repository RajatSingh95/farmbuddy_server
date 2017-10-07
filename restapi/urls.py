from django.conf.urls import include, url
from . import views

urlpatterns = [
    
    url( r'^$' , views.index , name='index' ),
    url( r'^farmerdetail/' , views.farmerdetail , name='farmerdetail' ),
    url( r'^mapdetail/' , views.mapdetail , name='mapdetail' ),
    url( r'^logindetail/' , views.logindetail , name='logindetail' ),
    url( r'^housedetail/' , views.housedetail , name='housedetail' ),
    url( r'^cropdetail/' , views.cropdetail , name='cropdetail' ),
    url( r'^welldetail/' , views.welldetail , name='welldetail' ),
]



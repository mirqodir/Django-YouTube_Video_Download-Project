from django.urls import path
from .views import *

urlpatterns = [ 

		path('',home,name='index'),
		path('download',download,name='download')


]
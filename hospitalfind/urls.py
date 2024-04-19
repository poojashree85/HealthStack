from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('', admin.site.urls),
    path('getdetails/',views.getdetails,name='getdetails'),
    #path('deletedetails/',views.deletedetails,name='deletedetails'),
    path('getdetails/<int:id>',views.getdetails,name='getdetails'),
    path('hospital',views.hospital,name='hospital'),
]

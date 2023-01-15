from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'), 
    #this is used when the urls.py calls this file with the address bar as localhost:port/
    path('bitArithmetic/', views.bitArithmetic, name='bitArithmetic'), 
    path('bitArithmetic/changeBinary', views.changeBinary, name="modify binary value"),
    path('bitArithmetic/changeHexa', views.changeHexa, name="modify hexa value"),
    path('bitArithmetic/allArithmetic', views.allArithmetic, name='all arithmetic operations'),

    path('bitShift/', views.bitShift, name="bit shifting"),
    path('bitShift/changeBinary', views.changeBinary, name="modify binary value"),
    path('bitShift/changeHexa', views.changeHexa, name="modify hexa value"),
    path('bitShift/allshiftings', views.allShiftings, name="all shifting operations"),

    path('bitRotate/', views.bitRotate, name="bit Rotate"),
    path('bitRotate/changeBinary', views.changeBinary,name='change binary value'),
    path('bitRotate/changeHexa',views.changeHexa,name='change hexa value'),
    path('bitRotate/allRotatings', views.allRotatings, name="all rotation operations"),

    #this is used when urls.py calls this file with the address bar as localhost:port/bitArithmetic
    path('baseConversions/', views.baseConversions, name="base conversions"),
    path('baseConversions/changeBinary', views.changeBinary, name="modify binary value"),
    path('baseConversions/changeHexa', views.changeHexa, name="modify hexa value"),
    path('baseConversions/allconversions', views.allconversions, name="all base conversions"),

    path('bitShiftRotate/', views.bitShiftRotate, name="bit shift rotate"),
    path('logicalOperations/',views.logicalOperations,name="logical operations"),
]
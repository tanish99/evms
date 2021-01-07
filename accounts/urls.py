"""evms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from . import views
from django.urls import path
from .views import *

urlpatterns = [
   path('register',views.register,name="register"),
    path('login',views.login,name="login"),
   path('logout',views.logout,name="logout"),
   path('dul',views.dul,name="dul"),
   path('getdata',views.getdata,name="getdata"),
   path('pdf/',GeneratePdf.as_view(),name="pdf"),
   path('vd',views.vd,name="vd"),
   path('ba',views.ba,name="ba")
  
   
]

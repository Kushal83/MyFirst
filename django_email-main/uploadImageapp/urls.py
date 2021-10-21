from django.contrib import admin
from django.urls import path,include
from uploadImageapp.views import *

urlpatterns = [
    
    path('uploadimage' ,  uploadimage  , name = "uploadimage"),
]
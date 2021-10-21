from django.contrib import admin
from django.urls import path,include
from register_details.views import *

urlpatterns = [
    path('insertapp' ,  insertapp  , name = "insertapp"),
]
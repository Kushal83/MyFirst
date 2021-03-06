from django.shortcuts import render,redirect
from register_details.models import Register_details
from rest_framework.views import APIView
from rest_framework.response import Response
from register_details.serialize import RegistrateSerialize
from rest_framework import status
from rest_framework.decorators import api_view
from register_details.databaseProvider.User_detailsCRUD import *


@api_view(['POST'])
def saveapp(request):
    if request.method == "POST":
        saveserialize = RegistrateSerialize(data=request.data)
        if saveserialize.is_valid():
            saveserialize.save()
            return Response(saveserialize.data,status=status.HTTP_201_CREATED)
            return Response(saveserialize.data , status = status.HTTP_400_BAD_REQUEST)
def insertapp(request):
    if not request.session.has_key("uid"):
        return redirect("/accounts/login")

    if request.method == "POST":
        uuid = request.session["uid"]        
        Firstname = request.POST.get('Firstname')
        Lastname = request.POST.get('Lastname')
        Address = request.POST.get('Address')
        City = request.POST.get('City')
        State = request.POST.get('State')
        Zip = request.POST.get('Zip')
        Company = request.POST.get('Company')
        CompanyAddress = request.POST.get('CompanyAddress')
        Phoneno = request.POST.get('Phoneno')
        data = {"uid":uuid , "Firstname":Firstname,
        "Lastname":Lastname,"Address":Address,
        "City":City, "State":State,"Zip":Zip,
        "Company":Company,"CompanyAddress":CompanyAddress,
        "Phoneno":Phoneno}
        dbuid = Validate_user_details(uuid)
        print(data)
        print(dbuid)
        if dbuid is not None and dbuid == uuid:
            updatedetails(data)
        else:
            insertdetails(data)
              
        return redirect('uploadimage')
    else:
        return render(request,'register_details.html')
                    
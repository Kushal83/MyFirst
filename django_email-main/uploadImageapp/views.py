from django.shortcuts import render

def index(request):
    return render(request , 'upload_doc.html')

def uploadimage(request):
    return render(request , 'upload_doc.html')
    
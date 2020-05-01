from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse
# get_objeect_or_404 --> to raise the error if not found
# redirect() --> used to redirect our web page
from .models import Main,fooAbout
# Create your views here.

def home(request):
    # sending dynamic data of title and footer about section
    qrr = fooAbout.objects.all()
    links = Main.objects.all()
    return render(request, 'home.html', {"title":"Home","site": qrr,"link":links})

def about(request):
    # sending dynamic data of title and footer about section
    qrr = fooAbout.objects.all()
    links = Main.objects.all()
    return render(request, 'about.html', {"title":"About","site": qrr,"link":links})

def json_data(request):
    qrr = Main.objects.values()
    take = list(qrr)
    return JsonResponse(take, safe=False)


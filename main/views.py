from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse
# get_objeect_or_404 --> to raise the error if not found
# redirect() --> used to redirect our web page
from .models import Main,fooAbout,about_main
from news.models import News
# Create your views here.

def home(request):
    # sending dynamic data of title and footer about section
    qrr = fooAbout.objects.all()
    links = Main.objects.all()
    new_news = News.objects.all()
    return render(request, 'front/home.html', {"title":"Home","site": qrr,"link":links,"news":new_news})

def about(request):
    # sending dynamic data of title and footer about section
    qrr = fooAbout.objects.all()
    brif = about_main.objects.all()
    links = Main.objects.all()
    return render(request, 'front/about.html', {"title":"About","site": qrr,"link":links,"details":brif})

def json_data(request):
    qrr = Main.objects.values()
    take = list(qrr)
    return JsonResponse(take, safe=False)


def panel(request):
    return render(request, 'back/home.html',{"title":"Admin | Home"})
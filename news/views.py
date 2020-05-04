from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse
from .models import News
from main.models import Main,fooAbout
# Create your views here.

def news_detail(request,word):
    news = News.objects.filter(name=word)
    qrr = fooAbout.objects.all()
    links = Main.objects.all()
    return render(request, 'news_detail.html',{'news':news,'title':news[0],"site": qrr,"link":links})
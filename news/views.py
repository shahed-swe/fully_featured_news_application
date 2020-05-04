from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse
from .models import News
# Create your views here.

def news_detail(request,pk):
    news = News.objects.filter(pk=pk)

    return render(request, 'news_detail.html',{'news':news,'title':news[0]})
from django.shortcuts import render,get_object_or_404,redirect
# get_objeect_or_404 --> to raise the error if not found
# redirect() --> used to redirect our web page
from .models import Main
# Create your views here.

def home(request):
    return render(request, 'home.html', {"title":"Home"})
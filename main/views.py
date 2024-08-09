from django.http import HttpRequest
from django.shortcuts import render

def index(request):
    return render(request,'main/index.html')

def about(request):
    return HttpRequest('about')
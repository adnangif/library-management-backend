from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

# Create your views here.


def login(request: HttpRequest):
    if(request.method == 'POST'):
        print(request.POST)
    return HttpResponse("adsfasdf")
    pass
from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_exempt
import json

from .utils import createUser
# Create your views here.


@csrf_exempt
def login(request: HttpRequest):
    if(request.method == 'POST'):
        x = json.loads(request.body)
        print(x)
        return HttpResponse("cookieafsdfasdf",status=200)
    elif(request.method == 'GET'):
        return HttpResponse("Aquired cookies")

@csrf_exempt
def signup(request: HttpRequest):
    if(request.method == "POST"):
        parsed = json.loads(request.body)
        print(parsed)
        result = createUser(parsed=parsed)

        if(result):
            return HttpResponse("Successfully received the given data")
        else:
            return HttpResponse("Error while creating account")
    else:
        return HttpResponse("This is not a post request")
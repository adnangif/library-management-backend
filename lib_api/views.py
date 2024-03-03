from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_exempt
import json
# Create your views here.


@csrf_exempt
def login(request: HttpRequest):
    if(request.method == 'POST'):
        x = json.loads(request.body)
        print(x)
        return HttpResponse("cookieafsdfasdf")
    elif(request.method == 'GET'):
        return HttpResponse("Aquired cookies")
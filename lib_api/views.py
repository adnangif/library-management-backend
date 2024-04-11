from urllib import response
from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import json
import jwt


from .utils import *




@api_view(['POST'])
def signup(request: HttpRequest):
    parsed = json.loads(request.body)
    print(parsed)
    result = createUser(parsed=parsed)

    if(result):
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['POST'])
def login (request: HttpRequest):
    parsed = json.loads(request.body)
    result = find_by_iid_and_password(parsed)
    
    if(result is not None and type(result) is dict):
        encoded_jwt = createJWT(result)

        return Response(status=status.HTTP_202_ACCEPTED,data={
            'token': encoded_jwt,
            })
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST,data={'error':"BAD REQUEST"})

    
@api_view(["GET"])
def user_info(request:HttpRequest):
    try:
        decoded = decodeJWT(request=request)
        return Response(status=status.HTTP_200_OK,data=decoded)
        
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_401_UNAUTHORIZED,data={"error":"token invalid"})





@api_view(['GET'])
def book_search(request:HttpRequest):
    pass

@api_view(['GET'])
def category_list(request:HttpRequest):
    pass

@api_view(['GET'])
def category_books(request:HttpRequest):
    pass

@api_view(['GET'])
def order_list(request:HttpRequest):
    pass

@api_view(["GET"])
def order_detaiils(request:HttpRequest):
    pass

@api_view(['GET'])
def book_details(request:HttpRequest):
    pass



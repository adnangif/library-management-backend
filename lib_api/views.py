from urllib import response
from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import json
import jwt


from .utils import *






@api_view(['POST'])
def login (request: HttpRequest):
    parsed = json.loads(request.body)
    # print(parsed)
    result = find_by_iid_and_password(parsed)
    


    if(result is not None and type(result) is dict):
        encoded_jwt = jwt.encode(result,JWT_SECRET)

        return Response(status=status.HTTP_202_ACCEPTED,data={
            'info': json.dumps(result),
            'token': encoded_jwt,
            })
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST,data={'error':"BAD REQUEST"})

    
@api_view(["GET"])
def user_info(request:HttpRequest):
    try:
        token:str = request.META["HTTP_AUTHORIZATION"]
        token = token.split(' ')[1]
        print(token)
        decoded = jwt.decode(jwt=token,key=JWT_SECRET,algorithms=["HS256"])
        print(decoded)
        return Response(status=status.HTTP_200_OK,data=decoded)

        
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_401_UNAUTHORIZED,data={"error":"token invalid"})


@api_view(['GET'])
def book_search(request:HttpRequest):
    pass




@api_view(['POST'])
def signup(request: HttpRequest):
    parsed = json.loads(request.body)
    print(parsed)
    result = createUser(parsed=parsed)

    if(result):
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
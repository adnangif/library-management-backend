from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import json
import jwt

jwt_secret = "aerpoic43sfd#$sfd%W$dsfSDfg#sdfg2#%$23dfs32ads12sdau7698gf*&hfd"

from .utils import createUser,find_by_iid_and_password

@api_view(['POST'])
def login (request: HttpRequest):
    parsed = json.loads(request.body)
    print(parsed)
    result = find_by_iid_and_password(parsed)
    


    if(result is not None and type(result) is dict):
        encoded_jwt = jwt.encode(result,jwt_secret)

        return Response(status=status.HTTP_202_ACCEPTED,data={
            'info': json.dumps(result),
            'token': encoded_jwt,
            })
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST,data={'error':"BAD REQUEST"})

    


@api_view(['POST'])
def signup(request: HttpRequest):
    parsed = json.loads(request.body)
    print(parsed)
    result = createUser(parsed=parsed)

    if(result):
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
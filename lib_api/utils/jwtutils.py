from django.http import HttpRequest, HttpResponse
from jwt import encode, decode
JWT_SECRET = "aerpoic43sfd#$sfd%W$dsfSDfg#sdfg2#%$23dfs32ads12sdau7698gf*&hfd"

def createJWT(payload:dict) -> str:
    return encode(payload=payload,key=JWT_SECRET)

def decodeJWT(request: HttpRequest) -> dict:
    token:str = request.META["HTTP_AUTHORIZATION"]
    token = token.split(' ')[1]
    return decode(jwt=token,key=JWT_SECRET,algorithms=["HS256"])

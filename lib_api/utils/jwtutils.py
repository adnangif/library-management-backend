from curses import keyname
import jwt
JWT_SECRET = "aerpoic43sfd#$sfd%W$dsfSDfg#sdfg2#%$23dfs32ads12sdau7698gf*&hfd"


def createJWT(payload:dict) -> str:
    return jwt.encode(payload=payload,key=JWT_SECRET)

def decodeJWT(jwt):
    decoded = jwt.decode(jwt=jwt,key=JWT_SECRET,algorithms=["HS256"])

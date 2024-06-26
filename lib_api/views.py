from urllib import response
from wsgiref.util import request_uri
from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import json
import jwt

from .utils import *


@api_view(['POST'])
def debug(request: HttpRequest):
    print(request.POST)
    print(request.POST.get('question-1'))

    return HttpResponse(request.POST)


@api_view(['POST'])
def signup(request: HttpRequest):
    parsed = json.loads(request.body)
    print(parsed)
    result = createUser(parsed=parsed)

    if (result):
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['POST'])
def login(request: HttpRequest):
    parsed = json.loads(request.body)
    result = find_by_iid_and_password(parsed)

    if (result is not None and type(result) is dict):
        encoded_jwt = createJWT(result)

        return Response(status=status.HTTP_202_ACCEPTED, data={
            'token': encoded_jwt,
        })
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': "BAD REQUEST"})


@api_view(["GET"])
def user_info(request: HttpRequest):
    try:
        decoded = decodeJWT(request=request)
        return Response(status=status.HTTP_200_OK, data=decoded)

    except Exception as e:
        print(e)
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={"error": "token invalid"})


@api_view(['GET'])
def book_search(request: HttpRequest):
    try:
        decoded = decodeJWT(request=request)

        q = request.GET.get('q')
        books = find_book_by_str(q)
        print(books)
        return Response(status=status.HTTP_200_OK, data=books)

    except Exception as e:
        print(e)
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={"error": "token invalid"})


@api_view(['GET'])
def category_list(request: HttpRequest):
    try:
        decoded = decodeJWT(request=request)

        categories = get_category_list()
        print(categories)
        return Response(status=status.HTTP_200_OK, data=categories)

    except Exception as e:
        print(e)
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={"error": "token invalid"})


@api_view(['GET'])
def category_books(request: HttpRequest):
    try:
        decoded = decodeJWT(request=request)

        category = request.GET.get('title')

        category_books = get_category_books(category)
        print(category_books)
        return Response(status=status.HTTP_200_OK, data=category_books)

    except Exception as e:
        print(e)
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={"error": "token invalid"})


@api_view(['GET'])
def available_count(request: HttpRequest):
    try:
        decoded = decodeJWT(request=request)

        info_id = request.GET.get('id')

        available_books = get_available_books_using_info_id(info_id)
        print(available_books)
        return Response(status=status.HTTP_200_OK, data=available_books)

    except Exception as e:
        print(e)
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={"error": "token invalid"})


@api_view(['POST'])
def create_order(request: HttpRequest):
    try:
        decoded = decodeJWT(request=request)
        parsed = json.loads(request.body)
        order = create_order_using_user_id(decoded["user_id"], parsed)

        print(order)
        return Response(status=status.HTTP_200_OK, data=order)

    except Exception as e:
        print(e)
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={"error": "token invalid"})


@api_view(['POST'])
def add_to_order(request: HttpRequest):
    try:
        decoded = decodeJWT(request=request)
        parsed = json.loads(request.body)

        result = add_book_to_order(parsed)

        print(result)
        return Response(status=status.HTTP_200_OK, data=result)

    except Exception as e:
        print(e)
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={"error": "token invalid"})


@api_view(['POST'])
def cancel_order(request: HttpRequest):
    try:
        decoded = decodeJWT(request=request)
        parsed = json.loads(request.body)

        result = delete_order(parsed)

        print(result)
        return Response(status=status.HTTP_200_OK, data=result)

    except Exception as e:
        print(e)
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={"error": "token invalid"})


@api_view(['GET'])
def order_list(request: HttpRequest):
    try:
        decoded = decodeJWT(request=request)

        result = get_orders(decoded['user_id'])

        print(result)
        return Response(status=status.HTTP_200_OK, data=result)

    except Exception as e:
        print(e)
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={"error": "token invalid"})


@api_view(["GET"])
def order_details(request: HttpRequest):
    try:
        decoded = decodeJWT(request=request)

        order_id = request.GET['id']
        user_id = decoded['user_id']

        result = get_order_details(order_id, user_id)

        print(result)
        return Response(status=status.HTTP_200_OK, data=result)

    except Exception as e:
        print(e)
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={"error": "token invalid"})


@api_view(['GET'])
def book_details(request: HttpRequest):
    try:
        decoded = decodeJWT(request=request)

        info_id = request.GET['id']

        result = get_book_details(info_id)

        print(result)
        return Response(status=status.HTTP_200_OK, data=result)

    except Exception as e:
        print(e)
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={"error": "token invalid"})


@api_view(["GET"])
def order_related_books(request: HttpRequest):
    try:
        decoded = decodeJWT(request=request)

        order_id = request.GET['id']

        result = get_related_books(order_id)

        print(result)
        return Response(status=status.HTTP_200_OK, data=result)

    except Exception as e:
        print(e)
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={"error": "token invalid"})


@api_view(['POST'])
def librarian_login(request: HttpRequest):
    parsed = json.loads(request.body)
    result = validate_librarian_iid_password(parsed)

    if (result is not None and type(result) is dict):
        encoded_jwt = createJWT(result)

        return Response(status=status.HTTP_202_ACCEPTED, data={
            'token': encoded_jwt,
        })
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': "BAD REQUEST"})


@api_view(["GET"])
def librarian_info(request: HttpRequest):
    try:
        decoded = decodeJWT(request=request)
        return Response(status=status.HTTP_200_OK, data=decoded)

    except Exception as e:
        print(e)
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={"error": "token invalid"})


@api_view(['POST'])
def librarian_signup(request: HttpRequest):
    parsed = json.loads(request.body)
    print(parsed)
    result = create_librarian(parsed=parsed)

    if (result):
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(["GET"])
def librarian_get_all_ordered_books(request: HttpRequest):
    try:
        decoded = decodeJWT(request=request)
        assert decoded.get('librarian_id') is not None

        data = get_all_ordered_books()
        return Response(status=status.HTTP_200_OK, data=data)

    except Exception as e:
        print(e)
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={"error": "token invalid"})


@api_view(["POST"])
def librarian_deliver_book(request: HttpRequest):
    try:
        decoded = decodeJWT(request=request)
        assert decoded.get('librarian_id') is not None

        parsed = json.loads(request.body)
        data = librarian_deliver_book_handle_db(parsed, decoded['librarian_id'])
        return Response(status=status.HTTP_200_OK,data=data)

    except Exception as e:
        print(e)
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={"error": "token invalid"})


@api_view(["GET"])
def librarian_get_all_borrowed_books(request: HttpRequest):

    try:
        decoded = decodeJWT(request=request)
        assert decoded.get('librarian_id') is not None

        data = get_all_borrowed_books()
        return Response(status=status.HTTP_200_OK, data=data)

    except Exception as e:
        print(e)
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={"error": "token invalid"})


@api_view(["POST"])
def librarian_receive_book(request: HttpRequest):
    try:
        decoded = decodeJWT(request=request)
        assert decoded.get('librarian_id') is not None

        parsed = json.loads(request.body)
        data = librarian_receive_book_handle_db(parsed, decoded['librarian_id'])
        return Response(status=status.HTTP_200_OK,data=data)

    except Exception as e:
        print(e)
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={"error": "token invalid"})


@api_view(['GET'])
def borrowed_books_by_user(request:HttpRequest):
    try:
        decoded = decodeJWT(request=request)
        user_id = decoded.get('user_id')
        assert user_id is not None

        data = get_user_borrowed_books(user_id=user_id)
        return Response(status=status.HTTP_200_OK, data=data)

    except Exception as e:
        print(e)
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={"error": "token invalid"})



@api_view(['GET'])
def waiting_list(request: HttpRequest):
    pass

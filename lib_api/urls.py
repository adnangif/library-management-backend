from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login),
    path('signup/',views.signup),
    path('user-info/',views.user_info),
]

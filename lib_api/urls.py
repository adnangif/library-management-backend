from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login),
    path('signup/',views.signup),
    path('user-info/',views.user_info),
    path('debug/',views.debug),
    path('search/',views.book_search),
    path('categories/',views.category_list),
    path('category/',views.category_books),
    path('available/',views.available_count),
    path('create-order/',views.create_order),
    path('book-order/',views.add_to_order),
    path('cancel-order/',views.cancel_order),
    path('orders/',views.order_list),
    path('order-details/',views.order_details),
    path('book-details/',views.book_details),
    
    
    path('order-related-books',views.order_related_books),
]

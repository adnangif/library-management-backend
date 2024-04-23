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
    path('ordered-books/',views.order_related_books),

    path('librarian/login/',views.librarian_login),
    path('librarian/signup/',views.librarian_signup),
    path('librarian/get-all-ordered-books/',views.librarian_get_all_ordered_books),
    path('librarian/deliver-book/',views.librarian_deliver_book),

]

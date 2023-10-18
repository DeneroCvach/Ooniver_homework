from django.urls import path
from my_app.views import index, square, admin_page, guest_page, check_role, login, booking, is_palindrome
from my_app.utils import prime

urlpatterns = [
    path('', index, name='index'),
    path("square/<int:number>", square, name='square'),
    path('prime/<int:number>', prime, name='prime'),
    path('admin-p/', admin_page, name='admin-page'),
    path('guest-p/<role>', guest_page, name='guest-page'),
    path('ch/<role>', check_role, name='check-role'),
    path('login', login, name='login'),
    path('booking', booking, name='booking'),
    path('palindrome/<word>', is_palindrome, name='is-palindrome'),
]

from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    date = datetime.now().isoformat()
    return HttpResponse(f"Hello, user. You entered at {date}")


def square(request, number):
    sq = number ** 2
    return HttpResponse(f"The square of the number {number} = {sq}")


def admin_page(request):
    return HttpResponse(
        f"<H1 align='center'>You enter like ADMIN</H1>"
    )


def guest_page(request, role):
    return HttpResponse(
        f"<H1 align='center'>You enter like {role}</H1>"
    )


def check_role(request, role):
    if role == 'admin':
        return redirect('https://gooogle.com')
    else:
        return redirect('guest-page', role=role)


def login(request):
    if request.method == 'POST':
        return redirect('admin-page')
    elif request.method == 'GET':
        page_number = request.GET.get('page_number')
        return redirect('guest-page', role=page_number)


def booking(request):
    if request.method == 'GET':
        return render(
            request=request,
            template_name='book_booking.html'
        )

    booking_data = {
        'book_name': {'lable': 'имя книги', 'value': request.POST.get("book_name")},
        'person_name': {'lable': 'имя человека', 'value': request.POST.get("person_name")},
        'booking_data': {'lable': 'время', 'value': request.POST.get("booking_data")}
    }

    # with open('booking magazine.txt', 'w') as f:
    #     for key, value in booking_data.items():
    #         f.write(f'{key}: {value}\n')

    return render(
       request=request,
       template_name='booking_data.html',
       context={'booking_data': booking_data}
    )


def is_palindrome(request, word):
    rev = word[::-1]
    if rev == word:
        word_half = len(word) // 2
        return HttpResponse(f"{word[:word_half]}")
    else:
        return redirect('index')

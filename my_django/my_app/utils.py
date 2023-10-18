from django.http import HttpResponse


def prime(request, number):
    prime_list = [2]
    for i in range(3, number + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in prime_list:
            if j * j - 1 > i:
                prime_list.append(i)
                break
            if (i % j == 0):
                break
        else:
            prime_list.append(i)

    return HttpResponse(f"Prime numbers is {', '.join(str(x) for x in prime_list)}.")

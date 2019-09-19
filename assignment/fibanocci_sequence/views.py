import timeit

from django.contrib import auth
from django.http import request, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control


def front_page(request):
    return render(request, 'front_page.html')

def result(request):
    return HttpResponse(render(request, 'front_page.html'))

def calculation(num):
    if num <= 0:
        return render(request, 'front_page.html')
    elif num == 1:
        return 1
    else:
        num1 = 1
        num2 = 1
        for i in range(2, num):
            temp = num1 + num2
            num1 = num2
            num2 = temp
        return num2


def fibanocci(request):
    result = 0
    time_taken = 0
    start_time = timeit.timeit()
    msg = 'Please enter an integer number greater than zero'
    try:
        val = int(request.POST['num'])
        result = calculation(val)
    except:
        return render(request, 'front_page.html', {'m': msg})

    else:
        end_time = timeit.timeit()
        time_taken = start_time - end_time
        return render(request, 'result.html', {
            'result': result,
            'time_taken': time_taken,


    })

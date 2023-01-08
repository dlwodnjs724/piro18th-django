from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('index page')


def hello(request):
    return render(request, 'users/hello.html')


def user_detail(request, pk):
    return render(request, 'users/user_detail.html', {
        'pk': pk,
    })

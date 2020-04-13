from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h3>Привет Мир!</h3>')

# def testr(request):
#     return  HttpResponse('<h3>Все вышло!</h3>')
from django.http import HttpResponse
from django.shortcuts import render

def home_page(requests):
    return HttpResponse('Ответ')
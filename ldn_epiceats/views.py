from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def test_message(request):
    return HttpResponse('test message')
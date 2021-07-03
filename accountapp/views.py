from django.http import HttpResponse
from django.shortcuts import render


def Hello_World(request):
    return HttpResponse("Hello World!")
# Create your views here.

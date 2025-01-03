from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello World")

def python(request):
    return HttpResponse("<h1>I'am Learning Python</h1>")
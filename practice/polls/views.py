from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def tester(passer):
    return HttpResponse("Hello world! You have reached the tester polls page at " + passer)

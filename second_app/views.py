from django.http import HttpResponse
from django.shortcuts import render

def list(request):
    return(HttpResponse('This is list of something'))

def graph(request):
    return(HttpResponse('This is graph'))

def hello(request):
    return(HttpResponse('Hello, Yurii'))
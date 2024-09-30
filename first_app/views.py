from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request


# Create your views here.
def index(request):
    return HttpResponse('Hello, ITcode!')
def catalog(request):
    return HttpResponse('Catalog')
from django.shortcuts import render
from django.http import HttpResponse

today = 'monday'
time_now = '00:23'
weather_now = 'Sunny'

def day(request):
    return(HttpResponse(f'Today is: {today}'))

def time(request):
    return(HttpResponse(f'Time is: {time_now}'))

def weather(request):
    return(HttpResponse(f'Weather now: {weather_now}'))

from django.urls import path

from second_app.views import list, graph, hello

urlpatterns=[
    path('list/', list),
    path('graph/', graph),
    path('hello/', hello)
    ]

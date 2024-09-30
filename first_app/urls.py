from django.urls import path

from first_app.views import index, catalog


urlpatterns=[
    path('', index),
    path('catalog/', catalog),
    ]
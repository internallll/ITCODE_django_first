from django.urls import path


from third_app.views import day,time, weather

urlpatterns=[
    path('day/', day),
    path('time/', time),
    path('weather/', weather)
]
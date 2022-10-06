from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('counters', views.counters, name='counters')
]
    
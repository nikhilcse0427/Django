from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('func/', views.func, name='func'),
    path('list_view/', views.list_view, name='list_view'),
    path('getval/<str:a>/<str:b>/', views.getval, name='getval'),
    path('query/', views.query, name='query'),
    path('jsonVal/', views.jsonVal, name='jsonVal'),  # added trailing slash (optional but recommended)
    path('getAPI/', views.getAPI, name='getAPI'),
    path('first/', views.first, name='first'),
    path('hello/', views.hello_world, name='hello'),
    path('one/', views.one, name='one'),
    path('incfile/', views.inc, name='incfile'),
    path('two/', views.two, name='two'),
]

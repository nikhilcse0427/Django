from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('func/', views.func),
    path('list_view/', views.list_view),
    path('getval/<str:a>/<str:b>/', views.getval),
    path('query/', views.query),
    path('jsonVal/', views.jsonVal),  # added trailing slash (optional but recommended)
    path('getAPI/', views.getAPI),
    path('first/', views.first),
]

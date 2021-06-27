
from django.contrib import admin
from django.urls import path
from appresupuesto import views

urlpatterns = [
    path('', views.main, name="home"),
]

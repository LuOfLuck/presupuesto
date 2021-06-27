
from django.contrib import admin
from django.urls import path
from appresupuesto import views
from django.conf.urls.static import static
urlpatterns = [
    path('presupuesto', views.main, name="home"),
]

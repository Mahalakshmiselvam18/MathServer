
from django.contrib import admin
from django.urls import path
from mahxapp import views

urlpatterns = [
    path('', views.churn_rate, name='Churn_rate'),
]
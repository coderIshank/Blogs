from .views import *
from django.urls import path

urlpatterns = [
    path('', hello, name='hello')
]
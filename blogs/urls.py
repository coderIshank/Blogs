from blogs.views import *
from django.urls import path

urlpatterns = [
    path('', hello, name='hello'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('blogs/', BlogView.as_view(), name='blogs'),

]
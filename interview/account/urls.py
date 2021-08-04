from django.urls import path
from .views import *

urlpatterns = [
    path('', MenuAPI.as_view(), name='menu')
]
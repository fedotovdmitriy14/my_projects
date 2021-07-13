from django.urls import path

from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    # path('main/', views.show_main, name='main'),
    path('models/', views.models, name='models'),
]
from django.urls import path

from home import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('about/', views.about),
]
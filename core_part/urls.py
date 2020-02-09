from django.urls import path

from core_part import views

urlpatterns = [
    path('', views.StartPageView, name = 'main')
]
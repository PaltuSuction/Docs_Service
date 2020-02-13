from django.conf.urls import url
from django.urls import path

from authentication_part import views

urlpatterns = [
    path('', views.Login, name = 'login'),

    url(r'registration/', views.Registration, name='registration'),

    url(r'^user/([0-9]{6})$', views.MainPage, name='main'),
]
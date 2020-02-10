from django.conf.urls import url
from django.urls import path

from authentication_part import views

urlpatterns = [
    path('', views.Login.as_view(), name = 'login'),

    url(r'registration/', views.Registration, name='registration')
]
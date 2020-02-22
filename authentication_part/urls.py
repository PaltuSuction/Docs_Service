from django.conf.urls import url
from django.urls import path, include

import core_part.views
from authentication_part import views

urlpatterns = [
    path('', views.startpageview, name='startpage'),
    #path(r'login/', views.Login, name ='login'),
    path(r'login/', views.login, name ='login'),
    url(r'logout/', views.logout.as_view(), name='logout'),
    url(r'registration/', views.Registration, name='registration'),

    #url(r'user/([0-9]{6})/', include('core_part.urls'), name='toUserPage'),
    #url(r'', include('core_part.urls'))
]
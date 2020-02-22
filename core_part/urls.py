from django.conf.urls import url
from django.urls import path

from core_part import views

urlpatterns = [

    url(r'parseExcel/', views.uploading_excel_view, name='parse_excel'),
    url(r'', views.MainPage, name='main'),


    path('task/<str:task_id>/', views.TaskView.as_view(), name='task'),

]
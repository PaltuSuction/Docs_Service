from django.conf.urls import url
from django.urls import path

from core_part import views

urlpatterns = [
    #path('', views.StartPageView, name = 'main')

    url(r'parseExcel/', views.upload_excel_file, name='parse_excel')
]
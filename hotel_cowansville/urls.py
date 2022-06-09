from django.urls import path

from . import views

app_name = 'hotel_cowansville'
urlpatterns = [
    path('', views.index, name='index'),
]
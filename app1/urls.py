from django.urls import path
from app1 import views


#create requests for app1 application

app_name = 'app1'

urlpatterns = [
    path('',views.app1,name='app1'),
]
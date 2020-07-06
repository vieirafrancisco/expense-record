from django.urls import path
from django.conf.urls import url
from users import views

app_name = 'users'
urlpatterns = [
    url('^dashboard/', views.dashboard, name='dashboard'),
]
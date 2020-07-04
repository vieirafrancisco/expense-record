from django.urls import path

from . import views

app_name = 'main_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('<int:user_id>/dashboard/', views.dashboard, name='dashboard')
]
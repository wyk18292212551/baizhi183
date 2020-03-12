from django.urls import path
from login import views
app_name='login'
urlpatterns=[
    path('login/', views.login, name='login'),
    path('quit/', views.quit, name='quit'),
    path('get_code/', views.get_code, name='get_code'),
    path('check_user/', views.check_user, name='check_user'),
]
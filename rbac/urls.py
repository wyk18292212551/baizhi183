from django.urls import path

from rbac import views
app_name="rbac"
urlpatterns = [
    path('login/',views.login),
    path('user_login/',views.user_login),
]
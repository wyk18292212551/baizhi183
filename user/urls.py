from django.urls import path
from user import views
app_name="user"
urlpatterns = [
    path('get_user_data/',views.get_user_data,name="get_user_data"),
    path('edit_user_data/',views.edit_user_data,name="edit_user_data"),
    path('qushi/',views.qushi,name="qushi"),
    path('get_map/',views.get_map,name="get_map"),
]

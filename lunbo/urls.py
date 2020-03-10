from django.urls import path

from lunbo import views
app_name="lunbo"
urlpatterns = [
    path('home/',views.home,name="home"),
    path('get_lunbo_data/',views.get_lunbo_data,name="get_lunbo_data"),
    path('edit_lunbo_data/',views.edit_lunbo_data,name="edit_lunbo_data"),
    path('add_lunbo_data/',views.add_lunbo_data,name="add_lunbo_data"),
]

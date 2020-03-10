from django.urls import path
from album import views
app_name="album"
urlpatterns = [
    path('get_album_data/',views.get_album_data,name='get_album_data'),

]

from django.urls import path
from album import views

app_name="album"

urlpatterns = [
    path('get_album_data/',views.get_album_data,name='get_album_data'),
    path('get_chapter_data/',views.get_chapter_data,name='get_chapter_data'),
    path('edit_album/',views.edit_album,name='edit_album'),
    path('edit_chapter/',views.edit_chapter,name='edit_chapter'),
    path('add_album/',views.add_album,name='add_album'),
    path('add_chapter/',views.add_chapter,name='add_chapter'),

]

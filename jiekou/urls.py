from django.urls import path
from jiekou import views
app_name="jiekou"
urlpatterns = [
    path('index_get/',views.index_get,name="index_get"),
    path('zhuanji_get/',views.zhuanji_get,name="zhuanji_get"),
    path('user_get/',views.user_get,name="user_get"),
    path('user_post/',views.user_post,name="user_post"),
]

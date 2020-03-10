from django.urls import path

from article import views
app_name="article"
urlpatterns = [
    path('getALLArticle/',views.getALLArticle),
    path('upload_img/',views.upload_img),
    path('query_img/',views.query_img),
    path('add_article/',views.add_article),
    path('xiugai/',views.xiugai),
    path('edit/',views.edit),
]

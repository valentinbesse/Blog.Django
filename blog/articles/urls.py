from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_articles, name='list_articles'),
    path('<int:article_id>/', views.detail_article, name='detail_article' ),
]
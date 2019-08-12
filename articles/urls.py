from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/results', views.results, name='results'),
    path('<int:article_id>/comment', views.comment, name='comment'),
]

from django.urls import path

from . import views

app_name = 'taxonomies'
urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:taxonomy_id>/', views.detail, name='detail'),
]

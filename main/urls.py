from django.urls import path
from .import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('index_abc_pk/<str:abc>/<int:pk>/', views.index_abc_pk, name='index_abc_pk'),  # выбираем ф-ию из файла
    path('index_path/<path:path>/', views.index_path, name='index_path'),  # выбираем ф-ию из файла
    path('list_main/', views.list_main, name='list_main'),
    path('form_create/', views.form_create, name='form_create'),
    path('result/', views.result, name='result'),
    path('table/', views.table, name='table'),
    path('table_filter/', views.table_filter, name='table_filter'),
    path('datetime_nov/', views.datetime_nov, name='datetime_nov'),
]

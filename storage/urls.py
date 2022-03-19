from django.urls import path
from . import views


app_name = 'storage'


urlpatterns = [
        path('', views.file_list, name='file_list'),
        path('<slug:category_slug>/', views.file_list, name='file_list_by_category'),
        path('<int:id>/<slug:slug>/', views.file_detail, name='file_detail'), ]

from django.urls import path
from . import views

app_name = 'ric'


urlpatterns = [
    path('', views.index, name='index'),
    path('list_radar/', views.list_radar, name='list_radar'),
    path('add_rls/', views.add_rls, name='add_rls'),
    path('<slug:radar>/', views.radar_detail, name='radar_detail'),

]

from django.urls import path
from . import views

app_name = 'ric'


urlpatterns = [
    path('', views.index, name='base'),
    path('list_radar/', views.list_radar, name='list_radar'),
    path('edit_rls/<int:pk>/', views.edit_rls, name='edit_rls'),
    path('add_rls/', views.add_rls, name='add_rls'),
    path('del_rls/<int:pk>/', views.del_rls, name='del_rls'),
    path('<slug:radar>/', views.radar_detail, name='radar_detail'),

]

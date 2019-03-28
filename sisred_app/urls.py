from django.urls import path, include
from . import views


app_name = 'sisred_app'

urlpatterns = [
    path('users/', views.get_all_users, name='allUsers'),
    path('users/<int:id>/', views.get_user_id_view, name='getUserId'),
    path('users/add/', views.add_user_view, name='addUser'),
    path('users/update/<int:id>/', views.update_user_view, name='updateUser'),
    path('reds/relacionados/<int:id>', views.get_reds_relacionados, name='reds_relacionados')

]
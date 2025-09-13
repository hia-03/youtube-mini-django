from django.urls import path

from .views import *

urlpatterns = [
    path('adduser/',create_user,name='created-user'),
    path('home/',home,name='home'),
    path('listuser/',user_list,name='list-user'),
    path('addvideo/',create_post,name='created-post'),
    path('listpost/',post_list,name='list-post'),
    path('updatepost/<int:id>',update_post,name='update-post'),
    path('delpost/<int:id>',delete_post,name='delete-post'),
    path('posts/<int:id>/', post_get_by_id, name='post-getbyid'),
    path('users/<int:id>/', user_get_by_id, name='usergetbyid'),
    path('updateuser/<int:id>',update_user,name='update-user'),
    path('deluser/<int:id>',delete_user,name='delete-user'),

]

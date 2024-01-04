# carpets/urls.py
from django.urls import path
from .views import post_list, post_detail
from django.urls import path
from .views import post_list, post_detail, post_create, post_update, post_delete
from .views import PostDeleteView

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
]
urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/create/', post_create, name='post_create'),
    path('post/<int:post_id>/update/', post_update, name='post_update'),
    path('post/<int:post_id>/delete/', post_delete, name='post_delete'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('current/', views.current_user),
    path('create/', views.create_user),
    path('update/', views.update_user),
    path('update/<int:user_id>', views.update_user_id),
    path('find/<int:user_id>', views.find_user_id),
    path('findall/', views.findall_user),
]
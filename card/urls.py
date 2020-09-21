from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_card),
    path('update/<int:card_id>', views.update_card_id),
    path('delete/<int:card_id>', views.delete_card_id),
    path('findall/', views.findall_card),
    path('find/user/', views.find_card_user),
    path('find/user/<int:user_id>', views.find_card_user_id),
    path('find/<int:card_id>', views.find_card_id)
]
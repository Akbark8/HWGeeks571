from django.urls import path
from . import views

urlpatterns = [
    path('', views.basket_list, name='basket_list'),
    path('add/', views.add_to_basket, name='add_to_basket'),
    path('update/<int:item_id>/', views.update_basket_item, name='update_basket_item'),
    path('delete/<int:item_id>/', views.delete_basket_item, name='delete_basket_item'),
]

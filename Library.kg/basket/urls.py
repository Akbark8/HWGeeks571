from django.urls import path
from . import views

urlpatterns = [

    path('', views.BasketListView.as_view(), name='basket_list'),
]

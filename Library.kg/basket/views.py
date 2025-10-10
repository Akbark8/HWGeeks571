from django.views.generic import ListView
from .models import BasketItem

class BasketListView(ListView):
    model = BasketItem
    template_name = 'basket/basket_list.html'  # потом создадим шаблон
    context_object_name = 'items'

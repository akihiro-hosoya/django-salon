from django.shortcuts import render
from django.views.generic import ListView
from .models import Item

# Create your views here.
class ItemListView(ListView):
    model = Item
    template_name = 'ec/item_list.html'
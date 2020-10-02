from django.urls import path
from ec import views

urlpatterns = [
    path('items/', views.ItemListView.as_view(), name='item_list'),
    path('item/<slug>', views.ItemDetailView.as_view(), name='item_detail'),
]
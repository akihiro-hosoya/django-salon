from django.urls import path
from ec import views

urlpatterns = [
    path('items/', views.ItemListView.as_view(), name='item_list'),
    path('item/<slug>', views.ItemDetailView.as_view(), name='item_detail'),
    path('additem/<slug>', views.addItem, name='additem'),
    path('order/', views.OrderView.as_view(), name='order'),
    path('removeitem/<slug>', views.removeItem, name='removeitem'),
    path('removesingleitem/<slug>', views.removeSingleItem, name='removesingleitem'),
    path('payment/', views.PaymentView.as_view(), name='payment'),
]
from django.urls import path
from ec import views

urlpatterns = [
    path('items/', views.ItemListView.as_view(), name='item_list'),
]
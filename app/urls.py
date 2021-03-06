from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('salon_choice/', views.SalonChoiceView.as_view(), name='salon_choice'),
    path('salon/<int:pk>', views.StylistChoiceView.as_view(), name='stylist_choice'),
    path('calendar/<int:pk>/', views.CalendarView.as_view(), name='calendar'),
    path('calendar/<int:pk>/<int:year>/<int:month>/<int:day>/', views.CalendarView.as_view(), name='calendar'),
    path('calendar/<int:pk>/<int:year>/<int:month>/<int:day>/<int:hour>/', views.BookingView.as_view(), name='booking'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
    path('booking/calendar/<int:year>/<int:month>/<int:day>/', views.BookingCalendarView.as_view(), name='booking_calendar'),
    path('mypage/holiday/<int:year>/<int:month>/<int:day>/<int:hour>/', views.Holiday, name='holiday'),
    path('mypage/delete/<int:year>/<int:month>/<int:day>/<int:hour>/', views.Delete, name='delete'),
    # About
    path('about/', views.AboutView.as_view(), name='about'),
    # Menu
    path('menu/', views.MenuView.as_view(), name='menu'),
    # News
    path('news/', views.NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
    # Stylist
    path('stylists/', views.StylistListView.as_view(), name='stylist_list'),
    path('stylist/<int:pk>/', views.StylistDetailView.as_view(), name='stylist_detail'),
    # Style
    path('style/', views.StyleListView.as_view(), name='style_list'),
    path('style/<int:pk>/', views.StyleDetailView.as_view(), name='style_detail'),
]
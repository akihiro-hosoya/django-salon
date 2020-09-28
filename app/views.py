from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import localtime, make_aware
from datetime import datetime, date, timedelta, time
from django.db.models import Q
from app.models import Salon, Stylist, Booking
from app.forms import BookingForm

# Create your views here.
class IndexView(TemplateView):
    template_name = "app/index.html"
    login_url = '/accounts/login/'

class SalonChoiceView(ListView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            start_date = date.today()
            weekday = start_date.weekday()
            # カレンダー日曜日開始
            if weekday != 6:
                start_date = start_date - timedelta(days=weekday + 1)
            return redirect('booking_calendar', start_date.year, start_date.month, start_date.day)
        
        salon_data = Salon.objects.all()

        return render(request, 'app/salon_choice.html', {
            'salon_data': salon_data,
        })

class StylistChoiceView(ListView):
    def get(self, request, *args, **kwargs):
        salon_data = get_object_or_404(Salon, id=self.kwargs['pk'])
        stylist_data = Stylist.objects.filter(salon=salon_data).select_related('user')

        return render(request, 'app/stylist_choice.html', {
            'salon_data': salon_data,
            'stylist_data': stylist_data,
        })

class CalendarView(View):
    def get(self, request, *args, **kwargs):
        stylist_data = Stylist.objects.filter(id=self.kwargs['pk']).select_related('user').select_related('salon')[0]
        today = date.today()
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        if year and month and day:
            # 週始め
            start_date = date(year=year, month=month, day=day)
        else:
            start_date = today
        # 1週間
        days = [start_date]
        days = [start_date + timedelta(days=day) for day in range(7)]
        start_day = days[0]
        end_day = days[-1]

        calendar = {}
        # 10時～20時
        for hour in range(10, 21):
            row = {}
            for day in days:
                row[day] = True
            calendar[hour] = row
        start_time = make_aware(datetime.combine(start_day, time(hour=10, minute=0, second=0)))
        end_time = make_aware(datetime.combine(end_day, time(hour=20, minute=0, second=0)))
        # 開始時間＜終了時間・終了時間＞開始時間
        booking_data = Booking.objects.filter(stylist=stylist_data).exclude(Q(start__gt=end_time) | Q(end__lt=start_time))
        for booking in booking_data:
            # 現地のタイムゾーンに変更
            local_time = localtime(booking.start)
            booking_date = local_time.date()
            booking_hour = local_time.hour
            if (booking_hour in calendar) and (booking_date in calendar[booking_hour]):
                calendar[booking_hour][booking_date] = False
        
        return render(request, 'app/calendar.html', {
            'stylist_data': stylist_data,
            'calendar': calendar,
            'days': days,
            'start_day': start_day,
            'end_day': end_day,
            'before': days[0] - timedelta(days=7),
            'next': days[-1] + timedelta(days=1),
            'today': today,
        })

class BookingView(View):
    def get(self, request, *args, **kwargs):
        stylist_data = Stylist.objects.filter(id=self.kwargs['pk']).select_related('user').select_related('salon')[0]
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        hour = self.kwargs.get('hour')
        form = BookingForm(request.POST or None)

        return render(request, 'app/booking.html', {
            'stylist_data': stylist_data,
            'year': year,
            'month': month,
            'day': day,
            'hour': hour,
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        stylist_data = get_object_or_404(Stylist, id=self.kwargs['pk'])
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        hour = self.kwargs.get('hour')
        start_time = make_aware(datetime(year=year, month=month, day=day, hour=hour))
        end_time = make_aware(datetime(year=year, month=month, day=day, hour=hour + 1))
        booking_data = Booking.objects.filter(stylist=stylist_data, start=start_time)
        form = BookingForm(request.POST or None)

        if booking_data.exists():
            form.add_error(None, '既に予約があります。\n別の日時で予約をお願いします。')
        else:
            if form.is_valid():
                booking = Booking()
                booking.stylist = stylist_data
                booking.start = start_time
                booking.end = end_time
                booking.name = form.cleaned_data['name']
                booking.furigana = form.cleaned_data['furigana']
                booking.tel = form.cleaned_data['tel']
                booking.remarks = form.cleaned_data['remarks']
                booking.save()
                return redirect('thanks')
        
        return render(request, 'app/booking.html', {
            'stylist_data': stylist_data,
            'year': year,
            'month': month,
            'day': day,
            'hour': hour,
            'form': form,
        })

class ThanksView(TemplateView):
    template_name = 'app/thanks.html'

class BookingCalendarView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        stylist_data = Stylist.objects.filter(id=request.user.id).select_related('user').select_related('salon')[0]
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        start_date = date(year=year, month=month, day=day)
        days = [start_date + timedelta(days=day) for day in range(7)]
        start_day = days[0]
        end_day = days[-1]

        calendar = {}
        # 10時～20時
        for hour in range(10, 21):
            row = {}
            for day_ in days:
                row[day_] = ""
            calendar[hour] = row
        start_time = make_aware(datetime.combine(start_day, time(hour=10, minute=0, second=0)))
        end_time = make_aware(datetime.combine(end_day, time(hour=20, minute=0, second=0)))
        booking_data = Booking.objects.filter(stylist=stylist_data).exclude(Q(start__gt=end_time) | Q(end__lt=start_time))
        for booking in booking_data:
            local_time = localtime(booking.start)
            booking_date = local_time.date()
            booking_hour = local_time.hour
            if (booking_hour in calendar) and (booking_date in calendar[booking_hour]):
                calendar[booking_hour][booking_date] = booking.first_name

        return render(request, 'app/booking_calendar.html', {
            'stylist_data': stylist_data,
            'booking_data': booking_data,
            'calendar': calendar,
            'days': days,
            'start_day': start_day,
            'end_day': end_day,
            'before': days[0] - timedelta(days=7),
            'next': days[-1] + timedelta(days=1),
            'year': year,
            'month': month,
            'day': day,
        })
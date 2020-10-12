from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from .models import Item, OrderItem, Order, Payment, Purchaser
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ItemListView(ListView):
    model = Item
    template_name = 'ec/item_list.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'ec/item_detail.html'

def addItem(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        ordered=False
    )
    order = Order.objects.filter(ordered=False)

    if order.exists():
        order = order[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        order = Order.objects.create(ordered_date=timezone.now())
        order.items.add(order_item)

    return redirect('order')

class OrderView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            order = Order.objects.get(ordered=False)
            context = {
                'order': order
            }
            return render(request, 'ec/order.html', context)
        except ObjectDoesNotExist:
            return render(request, 'ec/order.html')

def removeItem(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order = Order.objects.filter(
        ordered=False
    )
    if order.exists():
        order = order[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            return redirect("order")

    return redirect("product", slug=slug)

def removeSingleItem(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order = Order.objects.filter(
        ordered=False
    )
    if order.exists():
        order = order[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
                order_item.delete()
            return redirect("order")

    return redirect("item_detail", slug=slug)

class PaymentView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        order = Order.objects.get(ordered=False)
        form = PurchaserForm(
            request.POST or None,
        )
        return render(request, 'ec/payment.html')

    def post(self, request, *args, **kwargs):
        form = PurchaserForm(request.POST or None)
        purchaser_data = Purchaser.objects.get(blank=True, null=True)
        if form.is_valid():
            purchaser_name = form.cleaned_data['purchaser_name']
            purchaser_furigana = form.cleaned_data['purchaser_furigana']
            purchaser_adress = form.cleaned_data['purchaser_adress']
            purchaser_tel = form.cleaned_data['purchaser_tel']
            purchaser_email = form.cleaned_data['purchaser_email']
            purchaser_data.save()
            return redirect('order')

        order = Order.objects.get(ordered=False)
        order_items = order.items.all()
        amount = order.get_total()

        payment = Payment()
        payment.stripe_charge_id = 'test_stripe_charge_id'
        payment.amount = amount
        payment.save()

        order_items.update(ordered=True)
        for item in order_items:
            item.save()

        order.ordered = True
        order.payment = payment
        order.save()
        return redirect('thanks')
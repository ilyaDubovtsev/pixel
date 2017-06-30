from django.shortcuts import render
from django.utils import timezone
from .models import Order


# Create your views here.

def order_list(request):
    orders = Order.objects.filter(sended_date__lte=timezone.now()).order_by('sended_date')
    return render(request, 'orders/order.html', {'orders' : orders})

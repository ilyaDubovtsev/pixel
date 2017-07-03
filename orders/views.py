from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Order
from .forms import OrderForm


# Create your views here.

def landing(request):
    form = OrderForm()
    return render(request, 'orders/order.html', {'form': form})


def new_order(request):
    # orders = Order.objects.filter(sended_date__lte=timezone.now()).order_by('sended_date')\
    order = Order.objects.create()
    form = OrderForm(request.POST)
    if request.method == "POST":
        print('azazazazaza')
        print(request)
        if form.is_valid():
            order.email = request.POST.get('email')
            order.phone = request.POST.get('phone')
            order.text = request.POST.get('text')
            order.sended_date = timezone.now()
            order.save()
            return render(request, 'orders/success.html')
        else:
            return render(request, 'orders/order.html', {'form': form})
    else:
        return render(request, 'orders/order.html', {'form': form})


def success_order(request):
    return render(request, 'orders/success.html')

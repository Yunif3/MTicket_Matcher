from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order
# Create your views here.

def home(request):
    buys = Order.objects.filter(type = 'buy')
    sells = Order.objects.filter(type = 'sell')
    return render(request, 'home.html', {'buys' : buys, 'sells' : sells})
    
def order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.issuer = request.user
            order.save()
        return redirect('home')
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form' : form})
    
def contact(request, order_id):
    order = Order.objects.get(id = order_id)
    order.views += 1
    order.save()
    return render(request, 'contact.html', {'order' : order})
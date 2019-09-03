from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    buys = Order.objects.filter(type = 'buy').filter(status = 'a')
    sells = Order.objects.filter(type = 'sell').filter(status = 'a')
    return render(request, 'home.html', {'buys' : buys, 'sells' : sells})

@login_required
def order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.owner = request.user
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

@login_required
def dashboard(request):
    owned = Order.objects.filter(owner = request.user).exclude(status = 'w')
    return render(request, 'dashboard.html', {'owned' : owned })
 
@login_required 
def delete(request, order_id):
    order = Order.objects.get(id = order_id)
    if order.owner == request.user:
        order.status = 'w'
        order.save()
    return redirect('dashboard')
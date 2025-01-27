from django.shortcuts import render,redirect,get_object_or_404
from .models import Pizza,CartItem,Cart
from .forms import OrderForm
# Create your views here.

def menu_view(request):
    pizzas = Pizza.objects.all()
    return render(request,'menu/menu.html',{'pizzas':pizzas})

def order_view(request):
    total_price = 0
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            pizzas = form.cleaned_data['pizzas']
            total_price = int(sum(pizza.price for pizza in pizzas))
            form.save()
            # return redirect('menu')

    else:
        form = OrderForm()

    return render(request,'menu/order.html',{'form':form,'total_price':total_price})


def get_cart(request):
    cart = request.session.get('cart',{})
    return cart

def add_to_cart(request,pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    cart, created = Cart.objects.get_or_create(id=request.session.get('cart_id'))

    if created:
        request.session['cart_id'] = cart.id

    cart_item, created = CartItem.objects.get_or_create(cart=cart, pizza=pizza)

    if not created:
        cart_item.quantity += 1
        cart_item.save()


def cart_view(request):
    cart = get_cart(request)
    pizzas_in_cart = [(Pizza.objects.get(id=int(pid)),item) for pid,item in cart.items()]
    total_price = sum([float(item['price']) * item['quantity'] for item in cart.values()])
    return render(request,'menu/cart.html',{'pizzas_in_cart':pizzas_in_cart,'total_price': total_price})







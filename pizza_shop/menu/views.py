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

    if created or not request.session.get('cart_id'):

        request.session['cart_id'] = cart.id

    cart_item, created = CartItem.objects.get_or_create(cart=cart, pizza=pizza,defaults = {'quantity':1})

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')


def cart_view(request):
    cart_id = request.session.get('cart_id')
    if not cart_id:
        return render(request, 'menu/cart.html', {'pizzas_in_cart': [], 'total_price': 0})
    cart = get_object_or_404(Cart,id=cart_id)
    cart_items = CartItem.objects.filter(cart = cart)

    total_price = sum(item.total_price for item in cart_items)
    return render(request,'menu/cart.html',{'pizzas_in_cart':cart_items,'total_price': total_price})


def remove_from_cart(request,pizza_id):

    cart = get_cart(request)
    print(cart)
    cart_item = CartItem.objects.filter(cart=cart,pizza_id=pizza_id).first()
    if cart_item:
        if cart_item.quantity>1:
            cart_item.quantity-=1
            cart_item.save()
        else:
            cart_item.delete()

    return redirect('cart')





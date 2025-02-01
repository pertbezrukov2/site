from django.urls import path
from . import views


urlpatterns = [
    path('',views.menu_view,name ='menu'),
    path('order/',views.order_view,name = 'order'),
    path('add_to_cart/<int:pizza_id>/',views.add_to_cart,name = 'add_to_cart'),
    path('cart/',views.cart_view,name = 'cart'),
    path('remove_from_cart/<int:pizza_id>/',views.remove_from_cart,name ='remove_from_cart')
]

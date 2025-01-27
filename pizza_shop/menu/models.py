from django.db import models

# Create your models here.
class Pizza(models.Model):

    name = models.CharField(max_length=25)
    description = models.TextField(blank=True,null=True)
    photo = models.ImageField(upload_to='pizza_images/',blank=True,null=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)


    def __str__(self):
        return self.name


class Order(models.Model):
    customer_name = models.CharField(max_length=25)
    contact = models.CharField(max_length=100)
    address = models.TextField(blank=True,null=True)
    pizzas = models.ManyToManyField(Pizza)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заказ от{self.customer_name}-{self.created_at}"



class Cart(models.Model):
    pizzas = models.ManyToManyField(Pizza,through='CartItem')








class CartItem(models.Model):
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    @property
    def total_price(self):
        return self.pizza.price * self.quantity




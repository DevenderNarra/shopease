from django.db import models
from .user import User
from .product import Product
from .payment import Payment

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_customer': True})
    products = models.ManyToManyField(Product, through='OrderItem')
    payment=models.OneToOneField(Payment,on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    order_datetime = models.DateTimeField(auto_now_add=True)
    exp_delivery_date = models.DateField(blank=True, null=True)

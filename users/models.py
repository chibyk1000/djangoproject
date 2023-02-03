from django.db import models
from myapp.models import Product, Profile
from django.contrib.auth.models import User
from datetime import datetime
from django.conf  import settings
# Create your models here.
 
class OrderItem(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True )
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateField(auto_now=True)
    quantity = models.IntegerField(default=1)
    def __str__(self) -> str:
        return self.product.name

# class Cart(models.Model):
#     owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
   
#     created_at = models.DateTimeField(default=datetime.now)

class Order(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        items = models.ManyToManyField(OrderItem)
        start_date = models.DateTimeField(auto_now_add=True)
        ordered_date = models.DateTimeField()
        ordered = models.BooleanField(default=False)
        
        def __str__(self) -> str:
             return self.user.email
         
        def get_total_price(self):
            total = 0
            
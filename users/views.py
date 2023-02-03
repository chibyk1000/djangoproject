from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from myapp.models import Product
from .models import OrderItem, Order
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
# Create your views here.

def add_cart(request, pk):
   
    cart = Cart(request)
    product = Product.objects.get(id=pk)
    cart.add(product=product) 
    return JsonResponse({"message": "item added"})


def item_decrement(request, pk):
    cart = Cart(request)
    product = Product.objects.get(id=pk)
    cart.decrement(product=product)
    return JsonResponse({"message": "item decremented"})

def item_remove(request, pk):
    cart = Cart(request)
    product = Product.objects.get(id=pk)
    cart.remove(product)
    return JsonResponse({"message": "item removed"}) 


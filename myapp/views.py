from django.shortcuts import render, redirect, HttpResponse
import os
from .forms import RegistrationForm, ProductForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile, Product
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request): 
    products = Product.objects.all()
   
    return render(request, 'index.html', {"products": products})

def loginviews(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    form  = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html', {"form": form})

def signupviews(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    form = RegistrationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            
            messages.success(request, "registration successfull")
            return redirect('login')
            
        messages.error(request, "signup not successfull")
        return render(request, 'signup.html', {"form":form})
    
    
    return render(request, 'signup.html', {"form":form})

@login_required(login_url='login')
def adminviews(request):
    return render(request, "admin/dashboard.html")

@login_required(login_url='login')
def adminprofile(request,):
    image_url = request.user.profile.profile_pics.url
    print(image_url)
    username = request.user.username
    user =User.objects.get(username = username)
 
    
    return render(request, 'admin/profile.html', {"user": user, "url": image_url})

@login_required(login_url='login')
def logoutViews(request):
    
    logout(request)
    return  redirect('login')


@login_required(login_url='login')

def updateProfile(request):
    print(request.POST)
    if not request.POST:
        return HttpResponse('you are not authorized')
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    username = request.POST['username']
    email = request.POST['email']
    id = request.user.id
    user =User.objects.get(id = id)
    user.first_name = firstname
    user.last_name = lastname
    user.username = username
    user.email = email
    user.save()   
    return HttpResponse('profile updated successfully')
@login_required(login_url='login')
def updateProfilePics(request):
    if request.FILES:
        userid = request.user.id
        file = request.FILES['file']
        user_profile = Profile.objects.get(user = userid)
        
        user_profile.profile_pics.delete(False)
        user_profile.profile_pics = file
        user_profile.save()
        return redirect('admin-profile')
    return HttpResponse('it works')
    
@login_required(login_url='login') 
def add_product(request):
    form  = ProductForm()

    
    return render(request, 'admin/add-product.html', {"form": form})
def upload_product(request):
    form  = ProductForm()
    if not request.FILES or not request.POST:
        return render(request, 'admin/add-product.html', {"form": form})
    name = request.POST['name']
    price = request.POST['price']
    quantity = request.POST['quantity']
    description = request.POST['description']
    image = request.FILES['image']
    if name =="" or price == "" or quantity == "" or description == "" or image == "":
        messages.error(request, 'name or price or quantity or description is empty')
        return render(request, 'admin/add-product.html', {"form": form})
    product =Product(user_id =request.user.id ,name=name, price=price, quantity_available=quantity, image=image, description=description)
    product.save()
    return redirect('add_product')

def get_product(request, id):
    product = Product.objects.get(id=id)

    return render(request, 'product.html', {"product": product})

@login_required(login_url='login')
def products(request):
    products = Product.objects.all()
    return render(request, 'admin/products.html', {"products":products})
def view_cart(request):
    return render(request, 'cart.html')
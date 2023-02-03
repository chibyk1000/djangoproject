from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name="index"),
path('login/', views.loginviews, name='login'),
path('register/', views.signupviews, name="register"),
path('account/', views.adminviews, name="dashboard"),
path('profile/', views.adminprofile, name="admin-profile"), 
path('logout/', views.logoutViews, name="logout"), 
path('account/update-profile/', views.updateProfile, name="update-profile"), 
path('account/upload-pics/', views.updateProfilePics, name="upload-pics"), 
path('account/add-products/', views.add_product, name="add_product"), 
path('account/upload-products/', views.upload_product, name="upload_product"), 
path('product/<int:id>', views.get_product, name="product") ,
path('account/products', views.products, name="products"),
path('cart/', views.view_cart, name="cart")
]

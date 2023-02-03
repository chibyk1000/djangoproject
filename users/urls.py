from django.urls import path

from .import views
urlpatterns = [
path('cart/add/<int:pk>', views.add_cart, name="add_cart"),
path('cart/remove/<int:pk>', views.item_decrement, name="remove_cart"),
path('cart/delete/<int:pk>', views.item_remove, name="delete_cart"),

]
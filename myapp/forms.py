from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product
from django.contrib.auth import password_validation
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField
class RegistrationForm(UserCreationForm):
    firstname = forms.CharField(required=True, label="First Name", widget=forms.TextInput(attrs={'class': "mb-3 w-full"}))
    lastname = forms.CharField(required=True, label="Last Name", widget=forms.TextInput(attrs={'class': "mb-3 w-full"}))
     
    
    class Meta:
        model = User
        fields = ["firstname", "lastname", "username", "email"]
        

class ProductForm(forms.Form):
    name = forms.CharField(label="name")
    price = forms.IntegerField(label="Price")
    quantity_available = forms.IntegerField(label="Quantity Available")
    description = forms.CharField(label="description", widget=CKEditorWidget())
    image = forms.ImageField(label="Product Image")
    
    class meta:
        model = Product
        fields = ['name', 'price', 'quantity_avaliable', "image","description"]



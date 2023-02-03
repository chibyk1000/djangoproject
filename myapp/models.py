from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pics = models.ImageField(upload_to='user/', null=True, blank=True, default="default.jpg")
    def __str__(self) -> str:
        return self.user.username


CATEGORY =(
    ('P', 'Phones & Tablets'),
    ('C', 'Clothings'),
    ('E', 'Electronics')
)

class Product(models.Model):
    name = models.CharField(unique=True, max_length=255)
    image = models.ImageField(upload_to='product_img', null=False, blank=False)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY, max_length=2)
    quantity_available = models.IntegerField(null=True, blank=True, default="")
    description = RichTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
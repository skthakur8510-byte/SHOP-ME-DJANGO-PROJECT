from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
# Create your models here.
class categorys(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    price=models.FloatField(null=True,blank=True)
    category=models.ForeignKey(categorys,on_delete=models.CASCADE)
    img=models.ImageField(upload_to="img_media/",max_length=250,null=True,default=None)
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double Extra Large'),
        ('ALL','ALL SIZE'),
    ]
    size=models.CharField(max_length=5,choices=SIZE_CHOICES,default="ALL")

    def __str__(self): 
        return self.name
    








    
class mainimage(models.Model):
    img=models.ImageField(upload_to="main_image.jpeg/",max_length=250,null=True,default=None)

    def __str__(self):
        return str(self.img)
    




class Carousel(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='carousel/')
    
    def __str__(self):
        return self.title or f"Image {self.id}"
    


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_amount(self):
        return sum(item.total_price() for item in self.cartitem_set.all())

    def __str__(self):
        return f"Cart of {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=10, default='ALL')

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} ({self.size}) x {self.quantity}"


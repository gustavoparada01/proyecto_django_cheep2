from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html

# Create your models here.


class Post(models.Model):
    title = models.TextField(max_length=200)
    text = models.TextField()
    updated= models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    post =   models.ForeignKey(Post, on_delete=models.CASCADE)   
    updated= models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

class Pedido(models.Model):
    title = models.CharField(max_length=180)
    text = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Calzadoss(models.Model):
    imagess = models.ForeignKey('Imagess', related_name='imagen', on_delete=models.CASCADE)
    title = models.CharField(max_length=180)
    text = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

    
class Imagess(models.Model):
    title = models.CharField(max_length=180)
    image = models.ImageField(upload_to='imagen', null=True, blank=True)
    height_field = models.IntegerField(default=150)
    width_field = models.IntegerField(default=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

        



class Contenido(models.Model):
    title = models.CharField(max_length=180)
    text = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    


class CarouselImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='carousel_images/')
    description = models.TextField()

    def __str__(self):
        return self.title

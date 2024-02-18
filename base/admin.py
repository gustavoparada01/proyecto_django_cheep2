from django.contrib import admin

# Register your models here.

from .models import Post, Comment, Calzadoss, Pedido, Imagess, Contenido, CarouselImage

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Calzadoss)
admin.site.register(Pedido)
admin.site.register(Imagess)
admin.site.register(Contenido)
admin.site.register(CarouselImage)




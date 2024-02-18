from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

from .models import Post, Comment, Calzadoss, Pedido, Contenido, CarouselImage
from django.shortcuts import render


def calzadosPage(request):
    calzados = Calzadoss.objects.all()
    pedidos = Pedido.objects.all()  #  todos los  de Pedido
    if request.method == 'POST':
        Pedido.objects.create(
           title=request.POST.get('title'),
           text=request.POST.get('text')
        )

    return render(request, 'calzados.html', {'calzados': calzados, 'pedidos': pedidos})



    

def loginPage(request):
       if (request.method == 'POST'):
           username = request.POST.get('username')
           password = request.POST.get('password')
           if User.objects.filter(username=username).exists():
                user= authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Se inicio sesion correctamente' )
                    return redirect('home')
                     
           messages.error(request, 'Datos incorrectos')     
       return  render (request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        email = request.POST.get('email')
        name = request.POST.get('username')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if ( password != confirm_password) :
            messages.error(request, 'las contraseñas no coinciden')
            return redirect('/registro')
        User.objects.create_user(username, email=email, first_name=name, last_name=last_name,  password=password)
        return redirect('/login')
    return render(request,'register.html')


def home(request):
    contenido = Contenido.objects.all()
    carousel_items = CarouselImage.objects.all()  
    posts = Post.objects.order_by('-created')
    return  render(request, 'home.html', {'posts': posts,  'content': contenido, 'carousel_items': carousel_items})

def post(request, id = None):
    if request.method == 'POST':
        id= request.POST.get('id')
        if (id is None):
            Post.objects.create(
                title = request.POST.get('title'),
                text = request.POST.get('text'),
                user = request.user
            )
            messages.success(request, 'Mensaje creado correctamente' )
            return redirect('/')
        else:
            p = Post.objects.get(id = id)
            if(p.user == request.user):
                p.title = request.POST.get('title')
                p.text = request.POST.get('text')
                messages.success(request, 'Mensaje editado correctamente' )
                p.save()
                return redirect('home')

    context= {}
    if id is not None:
        p= Post.objects.get(id = id )
        context['post'] = p

    return  render (request, 'post.html', context)


def comment(request):
    p= Post.objects.get(id =  request.POST.get('post') )
    Comment.objects.create(
        text = request.POST.get('text'),
        user = request.user,
        post = p
    )
    return redirect('home')

def perfilPage(request):
    username = request.user.username
    return render(request, 'perfil.html', {'username': username})
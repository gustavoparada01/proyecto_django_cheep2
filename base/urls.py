from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home' ),
    path('login/', views.loginPage),
    path('registro/', views.registerPage),
    path('comment/', views.comment),
    path('logout/', views.logoutPage),
    path('post/', views.post),
    path('post/<int:id>', views.post),
    path('calzados/', views.calzadosPage),
    path('perfil/', views.perfilPage)
]
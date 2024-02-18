from django.http import JsonResponse
from ..models import Post, Calzadoss, Contenido 



def routes(request):
    routes = [
        'GET /api/posts',
        'GET /api/post/:id',
        'GET /api/calzadosAesthetic',
        'GET /api/contenidoInicio'
    ]
    return JsonResponse(routes, safe=False)

def  content(request):
    content = Contenido.objects.all()
    content_dict =[]
    for a in content:
        content_dict.append({
            'title': a.title,
            'text': a.text
            
        })
    return JsonResponse(content_dict, safe=False)

def posts(request):
    posts = Post.objects.all()
    posts_dict = []
    for p in posts:
        posts_dict.append({
            'title': p.title,
            'text': p.text,
            'id': p.id
        })
    return JsonResponse(posts_dict, safe=False)

def post(request, id):
    post = Post.objects.get(id=id)
    post_dict= {
            'title': post.title,
            'text': post.text,
            'id' : post.id
        }
    return JsonResponse(post_dict, safe=False)

def calzadoss(request):
    #pedidos = Pedido.objects.all()
    calzadoss = Calzadoss.objects.all()
    calzadoss_dict = []
    for c in calzadoss:
        calzadoss_dict.append({
            'title': c.title,
            'text': c.text,
            'id': c.id
        })
    return JsonResponse(calzadoss_dict, safe=False)





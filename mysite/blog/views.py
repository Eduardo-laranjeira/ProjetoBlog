from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comentario

def index(request):
    posts = Post.objects.all()
    context = {
        'posts_template': posts
    }
    return render(request, 'index.html', context)

def postagem(request, question_id):
    posts = Post.objects.get(id=question_id)
    context = {
        'posts_template': posts
    }
    return render(request, 'postagem.html', context)
from django.shortcuts import render
from django.http import Http404
from .models import Autor, Artigo

def index(request, username):
    try:
        pessoa = Autor.objects.filter(user=username)
    except:
        raise Http404('Arroba não encontrado')
    try:
        artigo = Artigo.objects.filter(autores=username)
    except:
        raise Http404('Artigo não encontrado')
    return render(request, 'iniciacao_cientifica/perfil.html', {'pessoa' : pessoa, 'artigo' : artigo})
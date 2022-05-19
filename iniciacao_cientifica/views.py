from django.shortcuts import render
from django.http import Http404
from .models import Autor, Artigo

def index(request, username):
    pessoa = Autor.objects.filter(user=username)
    if len(pessoa) == 0:
        raise Http404('Arroba não encontrado')
    artigo = Artigo.objects.filter(autores=username)
    if len(artigo) == 0:
        raise Http404('Autor não possui Artigos')
    return render(request, 'iniciacao_cientifica/perfil.html', {'pessoa' : pessoa, 'artigo' : artigo})

    '''
    try:
        pessoa = Autor.objects.filter(user=username)
    except Autor.DoesNotExist:
        raise Http404('Arroba não encontrado')
    try:
        artigo = Artigo.objects.filter(autores=username)
    except Artigo.DoesNotExist:
        raise Http404('Autor não possui Artigos')'''   
from django.shortcuts import render
from django.http import Http404
from .models import Aluno, Artigo

def index(request, username):

    try:
        pessoa = Aluno.objects.get(user=username)

    except Aluno.DoesNotExist:

        raise Http404('Nome de Usuário não encontrado')

    artigo = Artigo.objects.filter(autores=username)

    if len(artigo) == 0:
        
        return render(request, 'iniciacao_cientifica/perfil.html', {'pessoa' : pessoa, 'artigo' : 0})

    return render(request, 'iniciacao_cientifica/perfil.html', {'pessoa' : pessoa, 'artigo' : artigo})

    
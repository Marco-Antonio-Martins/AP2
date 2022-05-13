from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Autor

def index(request, username):
    try:
        pessoa = Autor.objects.filter(user=username)
    except pessoa.DoesNotExist:
        raise Http404('Arroba não encontrado')
    return render(request, 'iniciacao_cientifica/perfil.html', {'pessoa' : pessoa})
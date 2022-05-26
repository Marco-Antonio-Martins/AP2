from django.contrib import admin
from .models import Aluno, Artigo 

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    pass
@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    pass
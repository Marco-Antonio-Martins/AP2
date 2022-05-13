from django.contrib import admin
from .models import Autor, Artigo 

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    pass
@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    pass
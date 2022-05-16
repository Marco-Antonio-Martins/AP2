from django.db import models

class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=200)
    user = models.CharField('Nome de Usuário', max_length=25, primary_key=True)
    instituicao = models.CharField('Instituição', max_length=200)
    areas_interesse = models.CharField('Áreas de interesse', max_length=250)
    email = models.EmailField('E-mail')
    def __str__(self):
        return self.nome

class Autor(Aluno):
    pass

class Artigo(models.Model):
    titulo = models.CharField('Título', max_length=250)
    autores = models.ManyToManyField(Autor) 
    resumo = models.TextField('Resumo')
    data_publicacao = models.DateField('Data de publicação')
    evento = models.CharField('Evento', max_length=250)    
    def __str__(self):
        return self.titulo
from django.db import models

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    editora = models.CharField(max_length=200)
    ano_publicacao = models.IntegerField()
    numero_paginas = models.IntegerField()
    categoria = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    idioma = models.CharField(max_length=50)
    edicao = models.CharField(max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo


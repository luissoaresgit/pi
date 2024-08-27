from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Interesse(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo

class Sobre(models.Model):
    conteudo = models.TextField()
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)

    def __str__(self):
        return "Sobre"


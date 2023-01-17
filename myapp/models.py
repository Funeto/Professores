from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    choices_disciplina = (
        ('Língua Portugesa', 'Língua Portugesa'),
        ('Matemática', 'Matemática'),
        ('História', 'História'),
        ('Geografia', 'Geografia'),
        ('Biologia', 'Biologia'),
        ('Química', 'Química'),
        ('Física', 'Física'),
        ('Filosofia', 'Filosofia'),
        ('Sociologia', 'Sociologia'),
        ('Língua Inglesa', 'Língua Inglesa'),
        ('Artes', 'Artes'),
    )
    choices_area = (
        ('Ciências Exatas e da Terra', 'Ciências Exatas e da Terra'),
        ('Ciências Biológicas', 'Ciências Biológicas'),
        ('Ciências Humanas', 'Ciências Humanas'),
        ('Engenharias', 'Engenharias'),
        ('Ciências da Saúde', 'Ciências da Saúde'),
        ('Ciências Agrárias', 'Ciências Agrárias'),
        ('Linguística, Letras e Artes', 'Linguística, Letras e Artes'),
        ('Ciências Sociais e Aplicadas', 'Ciências Sociais e Aplicadas'),
    )
    choices_formacao = (
        ('Graduação', 'Graduação'),
        ('Pós-graduação', 'Pós-graduação'),
        ('Mestrado', 'Mestrado'),
        ('Doutorado', 'Doutorado'),
        ('Pós-doutorado', 'Pós-doutorado'),
    )
    disciplina = models.CharField(max_length=20, choices=choices_disciplina)
    area = models.CharField(max_length=40, choices=choices_area)
    formacao = models.CharField(max_length=20, choices=choices_formacao)

    def __str__(self):
        return (self.nome)
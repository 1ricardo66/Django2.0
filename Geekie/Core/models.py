from django.db import models
class Cpf(models.Model):
    cpf = models.CharField(max_length=11)
class Cadastro(models.Model):
    nome = models.CharField(max_length=60)
    email = models.CharField(max_length=120)
    cpf = models.OneToOneField(Cpf,on_delete=models.CASCADE)
    data_de_nascimento = models.DateField()
    senha = models.CharField(max_length=16)
    






# Create your models here.

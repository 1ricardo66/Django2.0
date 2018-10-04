from django.db import models
import math
from random import randint
#############################################################
#                                                           #
#                                                           #
#       IMPLEMENTAR UM METODO DE CATEGORIA DE CARROS        #
#       DEPENDENDO DA CATEGORIA MUDA O Valor DA HORA        #
#                                                           #
#                                                           #
#############################################################
class Cliente(models.Model):
    nome = models.CharField(max_length=60)
    data_de_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=180)
    Bairro = models.CharField(max_length=60)
    key = models.IntegerField()

    def __str__(self):
        return self.nome
    #Recebe todos os clientes 

class Veiculo(models.Model):
        nome = models.CharField(max_length=120,null=True,blank=True)
        modelo = models.CharField(max_length=120)
        placa = models.CharField(max_length=9)
        #Seta os veiculos em um form

        def __str__(self):
            content = (self.nome + ' - ' + self.placa)
            return content

class Parametros(models.Model):
    valor_hora = models.DecimalField(max_digits=5,decimal_places=2)
    valor_mes = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return "Parametros Gerais"

#Parametros editar depois

class MovRotativo(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    checkin = models.DateTimeField(auto_now=False)
    checkout = models.DateTimeField(auto_now=False)
    valor_hora = models.DecimalField(max_digits=5,decimal_places=2)
    veiculo = models.ForeignKey(Veiculo,on_delete=models.CASCADE)
    pago = models.BooleanField(default=False)

    def horas_total(self):

        return math.ceil((self.checkout - self.checkin).total_seconds() / 3600)
        #Função para pegar as horas /// Total_Seconds é uma função do Django

    def total (self):
        self.valor_total = self.valor_hora * self.horas_total()
        return ("%s R$"%self.valor_total)

    def __str__(self):
        return self.veiculo.placa


class Mensalista(models.Model):
    veiculo = models.ForeignKey(Veiculo,on_delete=models.CASCADE)
    inicio = models.DateField()
    valor_mes = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return str(self.veiculo) + ' - ' + str(self.inicio)

    #Mensalidade editar depois


class MovMensalista(models.Model):
    mensalista = models.ForeignKey(Mensalista,on_delete=models.CASCADE)
    data_pagamento = models.DateField()
    total = models.DecimalField(max_digits=5,decimal_places=2)

    #retorna o valor total no mes




# Create your models here.

from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=60)
    data_de_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=180)
    Bairro = models.CharField(max_length=60)
    key = models.IntegerField()

    def __str__(self):
        return self.nome


class Carro(models.Model):
        nome = models.CharField(max_length=120,null=True,blank=True)
        modelo = models.CharField(max_length=120)
        placa = models.CharField(max_length=9)


        def __str__(self):
            content = (self.nome + ' - ' + self.placa)
            return content

class Alugar(models.Model):
    STATUS_CHOICES = (
    ('Alugado','Alugado'),
    ('Reservado','Reservado'),
    ('Encerrado','Encerrado'),
    ('Completo','Completo'),
    )
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro,on_delete=models.CASCADE)
    alugado = models.DateField()
    devolucao = models.DateField()
    status = models.CharField(default='Completo',choices=STATUS_CHOICES,max_length=10)


    class Meta:
        verbose_name_plural = 'Alugar'

    def __str__(self):
        return self.cliente
# Create your models here.

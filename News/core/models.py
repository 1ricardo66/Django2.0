from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    cpf = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)

class New(models.Model):
    STATUS_CHOICES = (
    ('Published','Published'),
    ('Draft','Draft'),
    )
    title = models.CharField(max_length=120)
    date = models.DateTimeField()
    author = models.CharField(max_length=60)
    #author = models.ForeignKey(Author,on_delete=models.CASCADE)
    #author = models.ForeignKey(Author, on_delete=models.CASCADE)

    news = models.TextField()
    tags = models.CharField(max_length=120,blank=True)
    #||##############################################||#
    #||           Implementar Metodo de Tags V       ||#
    #||##############################################||#
    status = models.CharField(max_length=12,default="Draft",choices=STATUS_CHOICES)



# Editar o html , tentar pegar o checkbox true / false
# Create your models here.

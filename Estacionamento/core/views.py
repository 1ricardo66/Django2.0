from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def lista_pessoas(request):
    pessoa = Cliente.objects.all()
    context = {'cliente':pessoa}
    return render(request,'core/lista_pessoas.html',context)


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    context = {'veiculos':veiculos}
    return render(request,'core/lista_veiculos.html',context)


def movRotativo(request):
    mov_rot = MovRotativo.objects.all()
    context = {'mov_rot':mov_rot}
    return render(request,'core/mov_rotativo.html',context)
# Create your views here.

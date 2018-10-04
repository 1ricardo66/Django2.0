from django.shortcuts import render
from .models import Cadastro
def index(request):
    pessoa = Cadastro.objects.all()
    x=pessoa
    context = {'pessoa':pessoa,
    'x':x,}
    return render(request,'core/index.html',context)
# Create your views here.

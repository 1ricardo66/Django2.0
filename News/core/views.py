from django.shortcuts import render
from .models import New


def index (request):
    news = New.objects.all()
    news = news[::-1]
    context = { 'news':news }
    return render (request,'core/index.html',context)
# Create your views here.

from django.conf.urls import url,include
from django.urls import path
from .views import lista_pessoas,lista_veiculos,movRotativo
urlpatterns = [
    path('pessoas/',lista_pessoas, name='core_lista_pessoas'),
    path('veiculos/',lista_veiculos, name='lista_veiculos'),
    path('mov_rotativo/',movRotativo, name='mov_rotativo'),
]

from django.contrib import admin
from .models import (Cliente,
                     Veiculo,
                     Parametros,
                     MovRotativo,
                     Mensalista,
                     MovMensalista,
                     )

class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ("cliente","checkin","checkout","valor_hora",
    "pago","total","horas_total","veiculo",)

    def veiculo (self, obj):
        return obj.veiculo

    def cliente(self,obj):
        return obj.cliente

class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ("mensalista","data_pagamento","total",)


admin.site.register(Cliente)
admin.site.register(Veiculo)
admin.site.register(Parametros)
admin.site.register(Mensalista)
admin.site.register(MovMensalista,MovMensalistaAdmin)
admin.site.register(MovRotativo,MovRotativoAdmin)
# Register your models here.

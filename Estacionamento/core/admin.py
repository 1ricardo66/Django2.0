from django.contrib import admin
from .models import (Cliente,
                     Veiculo,
                     Parametros,
                     MovRotativo)

class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ("checkin","checkout","valor_hora","pago","total","horas_total")

admin.site.register(Cliente)
admin.site.register(Veiculo)
admin.site.register(Parametros)
admin.site.register(MovRotativo,MovRotativoAdmin)
# Register your models here.

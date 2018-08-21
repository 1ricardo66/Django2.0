from django.contrib import admin
from .models import (Cliente, Carro , Alugar,
                                            )

admin.site.register(Cliente)
admin.site.register(Carro)
admin.site.register(Alugar)
# Register your models here.

from django.contrib import admin

from .models import Orcamento

@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'endereco', 'servico', 'descricao', 'data', 'valor')

from django.contrib import admin
from import_export import resources 
from import_export.admin import ImportExportActionModelAdmin
from import_export.admin import ExportActionMixin
# Register your models here.

# Fornecedores
class ListandoFornecedores(admin.ModelAdmin):
    list_display = ('empresa','ramo_de_atividade')
    list_display_links = ('empresa',)
    search_fields = ('empresa',)
    list_per_page = 20
from .models import Fornecedore
admin.site.register(Fornecedore,ListandoFornecedores)

#Centros de Custo

class ListandoCentros(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'codigo_do_centro_de_custo')
    list_display_links = ('nome', 'codigo_do_centro_de_custo')
    list_filter = ('cnpj',)
    search_fields = ('codigo_do_centro_de_custo', 'nome',)
    list_per_page = 10
from .models import Centro_de_Custo
admin.site.register(Centro_de_Custo, ListandoCentros)


#Notas Fiscais
from .models import Notas_Fiscai
class RelatorioNota(resources.ModelResource):
    class Meta:
        model = Notas_Fiscai
        skip_unchanged = True
        report_skipped = False
        fields = ('codigo_NF', 'centro__codigo_do_centro_de_custo', 'fornecedor__empresa', 'data_de_emissao')

class ListandoNotas(ExportActionMixin, admin.ModelAdmin):
    def dataemissao(self, obj):
        return obj.data_de_emissao.strftime("%d/%m/%Y")
    def duplica_evento(ModelAdmin, request, queryset):
        for object in queryset:
            object.id = None
            object.save()
    duplica_evento.short_description = "Duplicar Nota Fiscal"

    resource_class = RelatorioNota
    list_display = ('codigo_NF', 'centro', 'fornecedor', 'dataemissao')
    list_display_links = ('codigo_NF',)
    search_fields = ('codigo_NF','fornecedor__empresa',)
    list_filter = ('data_de_emissao',)
    list_per_page = 20
    actions = ['duplica_evento']
from .models import Notas_Fiscai
admin.site.register(Notas_Fiscai, ListandoNotas)


#Produtos
from .models import Produto

# Impressão em tabela de Produtos ##

class RelatorioProduto(resources.ModelResource): 
    class Meta:
        model = Produto
        skip_unchanged = True
        report_skipped = False
        fields = ('tombamento', 'descricao', 'localizacao', 'nota_fiscal__codigo_NF', 'nota_fiscal__fornecedor__empresa', 'nota_fiscal__data_de_emissao','nota_fiscal__centro')

# Auxiliar de exportação e display de produtos ##

class RelatorioAdmin(ExportActionMixin, admin.ModelAdmin): 
    resource_class = RelatorioProduto
    def get_empresa(self,obj):
        return obj.nota_fiscal.fornecedor
    def get_dataemissao(self,obj):
        return obj.nota_fiscal.data_de_emissao.strftime("%d/%m/%Y")

    def duplica_evento(ModelAdmin, request, queryset):
        for object in queryset:
            object.id = None
            object.save()
    duplica_evento.short_description = "Duplicar Produto"
    def get_centrodecusto(self,obj):
        return obj.nota_fiscal.centro.codigo_do_centro_de_custo
    get_empresa.admin_order_field = 'nota_fiscal'
    get_empresa.short_description = 'Fornecedor'
    get_dataemissao.short_description = 'Data de Emissao'
    get_centrodecusto.short_description = 'Centro de Custo'
    list_display = ('tombamento', 'descricao', 'localizacao', 'nota_fiscal', 'get_empresa', 'get_dataemissao', 'get_centrodecusto')
    list_display_links = ('tombamento','descricao', 'nota_fiscal',)
    search_fields = ('tombamento', 'descricao',)
    list_filter = ('localizacao', 'nota_fiscal__fornecedor', 'nota_fiscal__data_de_emissao')
    list_per_page = 10
    actions = ['duplica_evento']
from .models import Produto
admin.site.register(Produto, RelatorioAdmin)

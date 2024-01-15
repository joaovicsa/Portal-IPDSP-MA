from django.db import models
from django.contrib import admin 

# Create your models here.



class Fornecedore(models.Model):
	
	empresa = 		models.CharField(verbose_name="Empresa",null=False, max_length = 100)
	nome_fantasia = 	models.CharField(verbose_name="Nome Fantasia:",null = True, max_length = 100)
	ramo_de_atividade = 	models.CharField(verbose_name="Ramo de Atividade:",null = True, max_length = 100)

	class Meta:
		verbose_name = "Fornecedor"
		verbose_name_plural = "Fornecedores"

	def __str__(self):
		return self.empresa
		

class Centro_de_Custo(models.Model):
	"""docstring for ClassName"""
	nome = 			models.CharField(verbose_name="Nome:",null = False, max_length = 50)
	cnpj = 			models.CharField(verbose_name="CNPJ", null = False, max_length = 18)
	codigo_do_centro_de_custo = models.CharField(verbose_name="Codigo do Centro de Custo:",null = False, max_length = 7)


	class Meta:
		verbose_name = "Centro de Custo"
		verbose_name_plural = "Centros de Custo"

	def __str__(self):
	 return self.nome

class Notas_Fiscai(models.Model):
	
	codigo_NF = 		models.CharField(verbose_name="Código da Nota:",max_length = 50, null = False)
	data_de_insercao = 	models.DateField(verbose_name="Data de Inserção:")
	data_de_emissao = 	models.DateField(verbose_name="Data de Emissão:")
	valor = 			models.DecimalField(null = False, max_digits = 10000, decimal_places = 2, help_text="Valor da Nota Fiscal")
	centro = 			models.ForeignKey(Centro_de_Custo, on_delete = models.CASCADE, null = False, verbose_name="Centro de Custo:")
	fornecedor = 		models.ForeignKey(Fornecedore, on_delete = models.CASCADE, null = False, verbose_name="Fornecedor")

	class Meta:
		verbose_name = "Nota Fiscal"
		verbose_name_plural = "Notas Fiscais"

	def __str__ (self):
		return (self.codigo_NF)



class Produto(models.Model):

	CATEGORIA_DE_PRODUTOS=models.TextChoices('Categoria do Produto','Máquinas Infomática Móveis')
	
	tombamento = 		models.CharField(max_length = 15, null = False, verbose_name="Tombamento:")
	descricao = 		models.CharField(verbose_name="Descrição:",max_length = 300, null = False)
	marca =				models.CharField(null=False, max_length=40, verbose_name="Marca:")
	valor = 			models.DecimalField(null = False, max_digits = 1000000, decimal_places = 2, help_text="Valor do Produto", verbose_name="Valor do Produto:")
	desconto = 			models.DecimalField(null=True, help_text="Insira o valor em Real.", decimal_places=2,max_digits=1000000, verbose_name="Desconto:")
	nmr_de_serie =		models.CharField(max_length=30, null=True, verbose_name="Número de Série:")
	nota_fiscal = 		models.ForeignKey(Notas_Fiscai, on_delete = models.CASCADE, null = False, verbose_name="Nota Fiscal:")	
	localizacao = 		models.CharField(verbose_name="Localização:",max_length = 200, null = False)
	situacao =			models.BooleanField(verbose_name="Situação:",help_text="Produto dado Baixa? Sim marque, não desmarque.")
	contabil =			models.BooleanField(verbose_name="Contábil?",help_text="Bem Contábel? Marque sim para verdadeiro.")
	categoria = 		models.CharField(max_length=50, null=False, choices=CATEGORIA_DE_PRODUTOS.choices, verbose_name="Categoria")
	origem_do_bem =		models.CharField(verbose_name="Origem do Bem:",max_length=100, null=False, help_text="Descrever Recurso Próprio ou nome do Convênio.")
	observacao = 		models.TextField(verbose_name="Observação:",max_length = 500, blank = True, null = True)

	class Meta:
		verbose_name = "Produto"
		verbose_name_plural = "Produtos"

	def __str__(self):
		return self.tombamento




from django.db import models

# Create your models here.

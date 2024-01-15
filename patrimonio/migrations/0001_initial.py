# Generated by Django 4.1.3 on 2022-11-08 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Centro_de_Custo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome:')),
                ('cnpj', models.CharField(max_length=18, verbose_name='CNPJ')),
                ('codigo_do_centro_de_custo', models.CharField(max_length=7, verbose_name='Codigo do Centro de Custo:')),
            ],
            options={
                'verbose_name': 'Centro de Custo',
                'verbose_name_plural': 'Centros de Custo',
            },
        ),
        migrations.CreateModel(
            name='Fornecedore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=100, verbose_name='Empresa')),
                ('nome_fantasia', models.CharField(max_length=100, null=True, verbose_name='Nome Fantasia:')),
                ('ramo_de_atividade', models.CharField(max_length=100, null=True, verbose_name='Ramo de Atividade:')),
            ],
            options={
                'verbose_name': 'Fornecedor',
                'verbose_name_plural': 'Fornecedores',
            },
        ),
        migrations.CreateModel(
            name='Notas_Fiscai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_NF', models.CharField(max_length=50, verbose_name='Código da Nota:')),
                ('data_de_insercao', models.DateField(verbose_name='Data de Inserção:')),
                ('data_de_emissao', models.DateField(verbose_name='Data de Emissão:')),
                ('valor', models.DecimalField(decimal_places=2, help_text='Valor da Nota Fiscal', max_digits=10000)),
                ('centro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patrimonio.centro_de_custo', verbose_name='Centro de Custo:')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patrimonio.fornecedore', verbose_name='Fornecedor')),
            ],
            options={
                'verbose_name': 'Nota Fiscal',
                'verbose_name_plural': 'Notas Fiscais',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tombamento', models.CharField(max_length=15)),
                ('descricao', models.CharField(max_length=300, verbose_name='Descrição:')),
                ('marca', models.CharField(max_length=20)),
                ('valor', models.DecimalField(decimal_places=2, help_text='Valor do Produto', max_digits=1000000)),
                ('desconto', models.DecimalField(decimal_places=2, help_text='Insira o valor em Real.', max_digits=1000000, null=True)),
                ('nmr_de_serie', models.CharField(max_length=30, null=True, verbose_name='Número de Série:')),
                ('localizacao', models.CharField(max_length=200, verbose_name='Localização:')),
                ('situacao', models.BooleanField(help_text='Produto dado Baixa? Sim marque, não desmarque.', verbose_name='Situação:')),
                ('contabil', models.BooleanField(help_text='Bem Contábel? Marque sim para verdadeiro.', verbose_name='Contábil?')),
                ('categoria', models.CharField(choices=[('Máquinas', 'Máquinas'), ('Infomática', 'Infomática'), ('Móveis', 'Móveis')], max_length=50)),
                ('origem_do_bem', models.CharField(help_text='Descrever Recurso Próprio ou nome do Convênio.', max_length=100, verbose_name='Origem do Bem:')),
                ('observacao', models.TextField(blank=True, max_length=500, null=True, verbose_name='Observação:')),
                ('nota_fiscal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patrimonio.notas_fiscai', verbose_name='Nota Fiscal:')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]
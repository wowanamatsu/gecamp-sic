# Generated by Django 2.0.7 on 2018-07-23 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('criado_em', models.DateTimeField(auto_now_add=True, null=True)),
                ('modificado_em', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Bairros',
                'db_table': 'bairros',
                'verbose_name': 'Bairro',
            },
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('criado_em', models.DateTimeField(auto_now_add=True, null=True)),
                ('modificado_em', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Cidades',
                'db_table': 'cidades',
                'verbose_name': 'Cidade',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, unique=True)),
                ('sigla', models.CharField(max_length=5, unique=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True, null=True)),
                ('modificado_em', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Estados',
                'db_table': 'estados',
                'verbose_name': 'Estado',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('criado_em', models.DateTimeField(auto_now_add=True, null=True)),
                ('modificado_em', models.DateTimeField(auto_now=True, null=True)),
                ('estado_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sic.Estado')),
            ],
            options={
                'verbose_name_plural': 'Municipios',
                'db_table': 'municipios',
                'verbose_name': 'Municipio',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=5, verbose_name='Código')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome')),
                ('nomeFormal', models.CharField(max_length=50, verbose_name='Nome formal')),
                ('fone', models.CharField(blank=True, max_length=5, null=True)),
                ('sigla', models.CharField(blank=True, max_length=4, null=True)),
                ('sigla2', models.CharField(blank=True, max_length=4, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True, null=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name_plural': 'Paises',
                'db_table': 'paises',
            },
        ),
        migrations.AddField(
            model_name='estado',
            name='pais_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sic.Pais'),
        ),
        migrations.AddField(
            model_name='cidade',
            name='municipio_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sic.Municipio'),
        ),
        migrations.AddField(
            model_name='bairro',
            name='cidade_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sic.Cidade'),
        ),
    ]
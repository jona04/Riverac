# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('uploaded_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Fornecedor',
                'verbose_name_plural': 'Fornecedores',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Jogadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nome')),
                ('last_name', models.CharField(max_length=50, verbose_name='Sobrenome')),
                ('nickname', models.CharField(max_length=10, verbose_name='Apelido')),
                ('position', models.IntegerField(choices=[(0, 'Goleiro'), (1, 'Zagueiro'), (2, 'Lateral'), (3, 'Volante'), (4, 'Meio Campo'), (5, 'Atacante')], null=True, verbose_name='Posição')),
                ('Nascimento', models.DateField(blank=True, verbose_name='Data de Nascimento')),
                ('height', models.FloatField(blank=True, null=True, verbose_name='Altura')),
                ('weight', models.DateTimeField(blank=True, null=True, verbose_name='Peso')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('uploaded_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Jogador',
                'verbose_name_plural': 'Jogadores',
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Parceiros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('uploaded_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Parceiro',
                'verbose_name_plural': 'Parceiros',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Patrocinadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('uploaded_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Patrocinador',
                'verbose_name_plural': 'Patrocinadores',
                'ordering': ['name'],
            },
        ),
    ]

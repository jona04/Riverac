# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 19:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonatos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('year', models.IntegerField(verbose_name='Ano')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('uploaded_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name_plural': 'Campeonatos',
                'verbose_name': 'Campeonato',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Estadios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('city', models.CharField(max_length=50, verbose_name='Cidade')),
                ('state', models.CharField(max_length=50, verbose_name='Estado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('uploaded_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name_plural': 'Estadios',
                'verbose_name': 'Estadio',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Partidas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Fora de casa'), (1, 'Dentro de casa')], default=0, verbose_name='Situação')),
                ('inside_or_outside', models.IntegerField(choices=[(0, 'Fora de casa'), (1, 'Dentro de casa')], null=True, verbose_name='Mando de campo')),
                ('start_date', models.DateTimeField(null=True, verbose_name='Inicio da Partida')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('uploaded_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('championship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partida_campeonato', to='partidas.Campeonatos', verbose_name='Campeonato')),
            ],
            options={
                'verbose_name_plural': 'Partidas',
                'verbose_name': 'Partida',
                'ordering': ['start_date'],
            },
        ),
        migrations.CreateModel(
            name='Times',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nome')),
                ('full_name', models.CharField(max_length=100, verbose_name='Nome Completo')),
                ('sigla', models.CharField(max_length=10, verbose_name='Sigla')),
                ('city', models.CharField(max_length=50, verbose_name='Cidade')),
                ('state', models.CharField(max_length=50, verbose_name='Estado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('uploaded_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name_plural': 'Campeonatos',
                'verbose_name': 'Campeonato',
                'ordering': ['first_name'],
            },
        ),
        migrations.AddField(
            model_name='partidas',
            name='opponent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partida_opponent', to='partidas.Times', verbose_name='Oponente'),
        ),
        migrations.AddField(
            model_name='partidas',
            name='stadium',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partida_estadio', to='partidas.Estadios', verbose_name='Estadio'),
        ),
    ]

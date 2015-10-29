# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='instruccion_mdl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instruccion', models.CharField(max_length=500, verbose_name=b'Comando')),
                ('descripcion', models.TextField(verbose_name=b'Descripci\xc3\xb3n', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='mdl_comandos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=500, verbose_name=b'Nombre')),
                ('favorito', models.BooleanField(default=False)),
                ('fechaIngreso', models.DateField(auto_now=True)),
                ('estado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='instruccion_mdl',
            name='comando',
            field=models.ForeignKey(to='comandos.mdl_comandos'),
        ),
    ]

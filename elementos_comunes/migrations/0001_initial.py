# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mdl_interfaz_aplicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Interfaz de aplicacion',
                'verbose_name_plural': 'Interfaz de aplicaciones',
            },
        ),
        migrations.CreateModel(
            name='mdl_lenguaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Lenguaje',
                'verbose_name_plural': 'Lenguajes',
            },
        ),
        migrations.CreateModel(
            name='mdl_nivel_desarrollo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Nivel de desarrollo',
                'verbose_name_plural': 'Nivel de desarrollos',
            },
        ),
        migrations.CreateModel(
            name='mdl_sistema_operativo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Sistema Operativo',
                'verbose_name_plural': 'Sistema Operativos',
            },
        ),
    ]

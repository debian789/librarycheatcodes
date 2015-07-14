# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('elementos_comunes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='mdl_proyectos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=500, verbose_name=b'Nombre')),
                ('descripcion', models.TextField(verbose_name=b'Descripci\xc3\xb3n', blank=True)),
                ('version', models.CharField(max_length=100, null=True, verbose_name=b'Version', blank=True)),
                ('link', models.URLField(max_length=300, null=True, verbose_name=b'Url', blank=True)),
                ('archivo', models.FileField(upload_to=b'archivoProyectos', null=True, verbose_name=b'Archivo Adjunto', blank=True)),
                ('favorito', models.BooleanField(default=False)),
                ('fechaIngreso', models.DateField(auto_now=True)),
                ('estado', models.BooleanField(default=False)),
                ('Nivel', models.ForeignKey(verbose_name=b'Nivel de Desarrollo', to='elementos_comunes.mdl_nivel_desarrollo')),
                ('interfaz', models.ForeignKey(verbose_name=b'Interfaz de Aplicaci\xc3\xb3n', to='elementos_comunes.mdl_interfaz_aplicacion')),
                ('lenguaje', models.ForeignKey(to='elementos_comunes.mdl_lenguaje')),
                ('os', models.ForeignKey(verbose_name=b'Sistema Operativo', to='elementos_comunes.mdl_sistema_operativo')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
            },
        ),
    ]

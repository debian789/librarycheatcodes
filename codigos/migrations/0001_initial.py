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
            name='mdl_codigos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=500)),
                ('descripcion', models.TextField(blank=True)),
                ('links', models.URLField(max_length=300, blank=True)),
                ('archivo', models.FileField(null=True, upload_to=b'archivoCodigos/', blank=True)),
                ('codigo', models.TextField()),
                ('favorito', models.BooleanField(default=False)),
                ('fechaIngreso', models.DateField(auto_now=True)),
                ('estado', models.BooleanField(default=False)),
                ('lenguaje', models.ForeignKey(to='elementos_comunes.mdl_lenguaje')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Codigo',
                'verbose_name_plural': 'Codigos',
            },
        ),
    ]

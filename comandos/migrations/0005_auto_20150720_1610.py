# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comandos', '0004_auto_20150715_1527'),
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
        migrations.RemoveField(
            model_name='comando_mdl',
            name='comando',
        ),
        migrations.RemoveField(
            model_name='mdl_comandos',
            name='descripcion',
        ),
        migrations.DeleteModel(
            name='comando_mdl',
        ),
        migrations.AddField(
            model_name='instruccion_mdl',
            name='comando',
            field=models.ForeignKey(to='comandos.mdl_comandos'),
        ),
    ]

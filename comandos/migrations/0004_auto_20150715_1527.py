# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comandos', '0003_auto_20150715_1519'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comando_mdl',
            options={},
        ),
        migrations.RemoveField(
            model_name='comando_mdl',
            name='comandos',
        ),
        migrations.AddField(
            model_name='comando_mdl',
            name='instruccion',
            field=models.CharField(default=1, max_length=500, verbose_name=b'Comando'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comando_mdl',
            name='comando',
            field=models.ForeignKey(to='comandos.mdl_comandos'),
        ),
    ]

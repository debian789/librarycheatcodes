# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comandos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comando_mdl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comando', models.CharField(max_length=500, verbose_name=b'Comando')),
            ],
        ),
        migrations.RemoveField(
            model_name='mdl_comandos',
            name='comando',
        ),
        migrations.AddField(
            model_name='comando_mdl',
            name='coamndos',
            field=models.ForeignKey(to='comandos.mdl_comandos'),
        ),
    ]

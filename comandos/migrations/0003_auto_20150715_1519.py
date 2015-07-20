# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comandos', '0002_auto_20150715_1515'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comando_mdl',
            options={'verbose_name': 'Comando', 'verbose_name_plural': 'Comandos'},
        ),
        migrations.AlterModelOptions(
            name='mdl_comandos',
            options={},
        ),
        migrations.RenameField(
            model_name='comando_mdl',
            old_name='coamndos',
            new_name='comandos',
        ),
    ]

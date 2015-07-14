# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codigos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mdl_favoritos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.ForeignKey(to='codigos.mdl_codigos')),
            ],
        ),
        migrations.CreateModel(
            name='mdl_mensajes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mensaje', models.CharField(max_length=500)),
            ],
        ),
    ]

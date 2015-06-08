# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mordor_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='PersonType',
            field=models.CharField(default='F', verbose_name='Tipo de pessoa', max_length=1, choices=[('F', 'Pessoa Física'), ('J', 'Pessoa Jurídica')]),
        ),
    ]

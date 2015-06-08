# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False)),
                ('sex', models.CharField(verbose_name='Sexo', default='M', choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('dob', models.DateField(verbose_name='Data de nascimento')),
                ('PersonType', models.CharField(verbose_name='Tipo pessoa', default='F', choices=[('F', 'Pessoa fÃ\xadsica'), ('J', 'Pessoa jurÃ\xaddica')], max_length=1)),
                ('cpfcnpj', models.CharField(verbose_name='CPF/CNPJ', max_length=36)),
            ],
            options={
                'verbose_name': 'User_Profile',
                'verbose_name_plural': 'User_Profiles',
            },
            bases=(models.Model,),
        ),
    ]

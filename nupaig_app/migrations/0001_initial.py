# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('cep', models.CharField(verbose_name='C.E.P.', max_length=10)),
                ('district', models.CharField(verbose_name='Bairro', max_length=50)),
                ('city', models.CharField(verbose_name='Estado', max_length=50)),
                ('complement', models.CharField(verbose_name='Complemento', max_length=60)),
                ('phone', models.CharField(verbose_name='Telefone', max_length=50)),
                ('cellphone', models.CharField(verbose_name='Celular', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'address',
                'verbose_name': 'address',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='dependence',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('dependence', models.CharField(verbose_name='Dependencia', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'dependences',
                'verbose_name': 'dependence',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='disease',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.CharField(verbose_name='Descrição', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'diseases',
                'verbose_name': 'disease',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.CharField(verbose_name='Descrição', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'events',
                'verbose_name': 'event',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='exam',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.CharField(verbose_name='Descrição', max_length=50)),
                ('print_cabec_exam', models.IntegerField(verbose_name='Imprime resultado no cabeçalho ?', choices=[(0, 'Não'), (1, 'Sim')])),
                ('export_results', models.IntegerField(verbose_name='Imprime resultado no cabeçalho ?', choices=[(0, 'Não'), (1, 'Sim')])),
                ('week_evolution', models.IntegerField(verbose_name='Imprime resultado no cabeçalho ?', choices=[(0, 'Não'), (1, 'Sim')])),
                ('type_exam', models.IntegerField(verbose_name='Imprime resultado no cabeçalho ?', choices=[(0, 'Sangue'), (1, 'Patologia'), (1, 'Imagem')])),
            ],
            options={
                'verbose_name_plural': 'exams',
                'verbose_name': 'exam',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='exam_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.CharField(verbose_name='Descrição', max_length=50)),
                ('type_exam_det', models.IntegerField(verbose_name='Tipo exame', choices=[(0, 'Qualitativo'), (1, 'Quantitativo')])),
                ('exam_id', models.ForeignKey(to='nupaig_app.exam')),
            ],
            options={
                'verbose_name_plural': 'exam_details',
                'verbose_name': 'exam_detail',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='exam_detail_exam_detail_qualit',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('exam_detail_id', models.ForeignKey(to='nupaig_app.exam_detail')),
            ],
            options={
                'verbose_name_plural': 'exam_detail_exam_detail_qualits',
                'verbose_name': 'exam_detail_exam_detail_qualit',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='exam_detail_qualit',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.CharField(verbose_name='Descrição', max_length=50)),
                ('exam_detail_qualit', models.ManyToManyField(through='nupaig_app.exam_detail_exam_detail_qualit', to='nupaig_app.exam_detail')),
            ],
            options={
                'verbose_name_plural': 'exam_detail_qualits',
                'verbose_name': 'exam_detail_qualit',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='pathology',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.CharField(verbose_name='Descrição', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'pathologys',
                'verbose_name': 'pathology',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Nome', max_length=80)),
                ('dob', models.DateField(auto_now_add=True)),
                ('sex', models.CharField(max_length=1, choices=[('M', 'Maculino'), ('F', 'Feminino')])),
                ('sign_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'persons',
                'verbose_name': 'person',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='person_address',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('address_id', models.ForeignKey(to='nupaig_app.address')),
                ('person_id', models.ForeignKey(to='nupaig_app.person')),
            ],
            options={
                'verbose_name_plural': 'person_address',
                'verbose_name': 'person_address',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='risk',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.CharField(verbose_name='Descrição', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'risks',
                'verbose_name': 'risk',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='standard_form',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.CharField(verbose_name='Descrição', max_length=50)),
                ('text', models.TextField(verbose_name='Texto', max_length=500)),
            ],
            options={
                'verbose_name_plural': 'standard_forms',
                'verbose_name': 'standard_form',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='suspension_reason',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.CharField(verbose_name='Descrição', max_length=50)),
                ('reason', models.IntegerField(verbose_name='Solicita motivo', default=0, choices=[(0, 'Não'), (1, 'Sim')])),
            ],
            options={
                'verbose_name_plural': 'suspension_reasons',
                'verbose_name': 'suspension_reason',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='transmition',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.CharField(verbose_name='Descrição', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'transmitions',
                'verbose_name': 'transmition',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.CharField(verbose_name='Descrição', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'treatments',
                'verbose_name': 'treatment',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='treatment_place',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.CharField(verbose_name='Descrição', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'treatment_places',
                'verbose_name': 'treatment_place',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='unit_measure',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('unit', models.CharField(verbose_name='Cód. Unidade', max_length=10)),
                ('description', models.CharField(verbose_name='Descrição', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'unit_measures',
                'verbose_name': 'unit_measure',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='exam_detail_exam_detail_qualit',
            name='exam_detail_qualit_id',
            field=models.ForeignKey(to='nupaig_app.exam_detail_qualit'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exam_detail',
            name='unit_measure_id',
            field=models.ForeignKey(to='nupaig_app.unit_measure', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='address',
            field=models.ManyToManyField(through='nupaig_app.person_address', to='nupaig_app.person'),
            preserve_default=True,
        ),
    ]

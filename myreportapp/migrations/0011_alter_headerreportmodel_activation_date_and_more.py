# Generated by Django 5.1 on 2024-10-20 18:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myreportapp', '0010_headerreportmodel_occurrence_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headerreportmodel',
            name='activation_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data do Acionamento'),
        ),
        migrations.AlterField(
            model_name='headerreportmodel',
            name='designation_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data de Designação'),
        ),
        migrations.AlterField(
            model_name='headerreportmodel',
            name='expert_display_name',
            field=models.CharField(default='', max_length=200, verbose_name='Perito'),
        ),
        migrations.AlterField(
            model_name='headerreportmodel',
            name='occurrence_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data da Ocorrência'),
        ),
        migrations.AlterField(
            model_name='headerreportmodel',
            name='report_date',
            field=models.DateField(auto_now_add=True, verbose_name='Data do Registro'),
        ),
        migrations.AlterField(
            model_name='headerreportmodel',
            name='service_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data do Atendimento'),
        ),
    ]

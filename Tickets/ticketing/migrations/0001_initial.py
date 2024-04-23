# Generated by Django 5.0.4 on 2024-04-23 18:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('nivel', models.SmallIntegerField(choices=[(1, 'NIVEL 1'), (2, 'NIVEL 2'), (3, 'NIVEL 3'), (4, 'NIVEL 4')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.CharField(max_length=300)),
                ('mensaje', models.TextField()),
                ('estado', models.CharField(choices=[('O', 'ABIERTO'), ('P', 'PENDIENTE'), ('C', 'COMPLETADO')], max_length=1)),
                ('prioridad', models.PositiveSmallIntegerField()),
                ('creacion', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketing.categoria')),
            ],
        ),
    ]
# Generated by Django 3.2.6 on 2021-08-15 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, null=True, verbose_name='Nome')),
                ('numero', models.IntegerField(null=True, verbose_name='Número')),
                ('estado', models.CharField(choices=[('Disponível', 'Disponível'), ('Ocupado', 'Ocupado'), ('Indisponível', 'Indisponível')], default=('Disponível', 'Disponível'), max_length=30, null=True, verbose_name='Estado')),
            ],
        ),
    ]

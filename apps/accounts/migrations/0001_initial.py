# Generated by Django 3.1 on 2020-09-01 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firs_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=220, null=True)),
                ('document', models.CharField(blank=True, max_length=15, null=True)),
                ('number', models.CharField(blank=True, max_length=20, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
                'ordering': ['firs_name'],
            },
        ),
    ]

# Generated by Django 3.1 on 2020-10-13 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201008_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile', verbose_name='Imagen de Perfil'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='document',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Número de Documento'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='firs_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombres'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=220, null=True, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Celular'),
        ),
    ]

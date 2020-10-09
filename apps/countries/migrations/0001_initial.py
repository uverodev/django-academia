# Generated by Django 3.1 on 2020-10-08 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('nom', models.CharField(blank=True, max_length=100, null=True)),
                ('iso2', models.CharField(blank=True, max_length=2, null=True)),
                ('iso3', models.CharField(blank=True, max_length=3, null=True)),
                ('phone_code', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'verbose_name': 'Pais',
                'verbose_name_plural': 'Paises',
                'ordering': ['id'],
            },
        ),
    ]

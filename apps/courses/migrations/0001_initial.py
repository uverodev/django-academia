# Generated by Django 3.1 on 2020-08-16 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Nombre de la Categoria')),
                ('order', models.IntegerField(default=5, verbose_name='Orden de Prioridades')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del Instructor')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Nombre de la Categoria')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('video', models.URLField(verbose_name='Video de Presentación')),
                ('image', models.ImageField(blank=True, null=True, upload_to='categorias', verbose_name='Imagen de Presentación')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True, verbose_name='Estado')),
                ('category', models.ManyToManyField(to='courses.Category')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='courses.instructor')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'ordering': ['date_created'],
            },
        ),
    ]

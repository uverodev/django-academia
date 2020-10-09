from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Nombre de la Categoria', max_length = 100, blank = False, null = False)
    order = models.IntegerField('Orden de Prioridades', blank = False, null = False, default = 5)
    date_created = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ["order"]
    
    def __str__(self):
        return self.name


class Instructor(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Nombre del Instructor', max_length = 100, blank = False, null = False)
    date_created = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructores'
    
    def __str__(self):
        return self.name

class Course(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Nombre del Curso', max_length = 100, blank = False, null = False)
    description = models.TextField('Descripción', blank = False, null = False)
    category = models.ManyToManyField(Category)
    instructor = models.ForeignKey(Instructor, on_delete=models.DO_NOTHING)
    video = models.CharField('Video de Presentación', max_length=20, blank = False, null = False)
    image = models.ImageField('Imagen de Presentación', upload_to='courses', blank = True, null = True)
    qualification = models.SmallIntegerField('Calificación', blank = False, null = False, default = 0)
    price = models.SmallIntegerField('Precio', blank = False, null = False, default = 10)
    date_created = models.DateTimeField(auto_now_add = True)
    status = models.BooleanField('Estado', default = True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ["date_created"]
    
    def __str__(self):
        return "{}, {}".format(self.name, self.qualification)
from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key = True)
    firs_name = models.CharField(max_length = 200, blank = False, null = False)
    last_name = models.CharField(max_length = 220, blank = False, null = False)
    number = models.CharField(max_length = 20, blank = False, null = False)
    descripcion = models.TextField(blank = False,null = False)
    estado = models.BooleanField('Estado', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['firs_name']

    def __str__(self):
        return self.firs_name

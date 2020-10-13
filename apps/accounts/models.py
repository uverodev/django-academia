from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    firs_name = models.CharField('Nombres', max_length = 200, blank = True, null = True)
    last_name = models.CharField('Apellidos', max_length = 220, blank = True, null = True)
    document = models.CharField('Número de Documento', max_length = 15, blank = True, null = True)
    number = models.CharField('Celular', max_length = 20, blank = True, null = True)
    descripcion = models.TextField('Descripcion', blank = True, null = True)
    image = models.ImageField('Imagen de Perfil', upload_to='profile', blank = True, null = True)
    estado = models.BooleanField('Estado', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['last_name']

    def __str__(self):
        return "{}, {}".format(self.firs_name, self.last_name)


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print("Se acaba de crear un usuario y su perfil enlazado")
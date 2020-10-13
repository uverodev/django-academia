from django.db import models
from apps.courses.models import Course
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Opinion(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    opinion = models.TextField('Opinión', blank = False, null = False)
    qualification = models.SmallIntegerField('Calificación', blank = False, null = False, default = 0)
    date_created = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'Opinión'
        verbose_name_plural = 'Opiniones'
        ordering = ["id"]

    def __str__(self):
        return "{} - {}".format(self.qualification, self.user.username, self.date_created)


@receiver(post_save, sender=Opinion)
def opinion_post_save(sender, instance, **kwargs):
    opiniones = Opinion.objects.filter(course = instance.course)
    sum=0
    cont=0
    for opi in opiniones:
        sum = sum + opi.qualification
        cont = cont + 1

    curso = Course.objects.get(id = instance.course.id)
    curso.qualification = sum/cont
    curso.save()
    print("El promedio es:")
    print(sum/cont)
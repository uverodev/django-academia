from django.db import models

class Country(models.Model):
    nombre = models.CharField(max_length = 100, blank = True, null = True)
    name = models.CharField(max_length = 100, blank = True, null = True)
    nom = models.CharField(max_length = 100, blank = True, null = True)
    iso2 = models.CharField(max_length = 5, blank = True, null = True)
    iso3 = models.CharField(max_length = 6, blank = True, null = True)
    phone_code = models.CharField(max_length = 10, blank = True, null = True)

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
        ordering = ['id']
from django.contrib import admin
from .models import Country
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CountryResource(resources.ModelResource):
    class Meta:
        model = Country

class CountryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre', 'iso2', 'iso3', 'phone_code')
    resourse_class = CountryResource

admin.site.register(Country, CountryAdmin)
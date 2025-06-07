from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . models import Vigilance, Complainant
# Register your models here.


admin.site.register(Vigilance, ImportExportModelAdmin)
admin.site.register(Complainant)



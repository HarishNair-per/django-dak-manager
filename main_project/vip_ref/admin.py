from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . models import HOD, Reference, VIP
# Register your models here.

admin.site.register(HOD)
admin.site.register(Reference, ImportExportModelAdmin)
admin.site.register(VIP, ImportExportModelAdmin)


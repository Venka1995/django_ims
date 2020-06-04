from django.contrib import admin
from .models import Laptop,Mobile,Desktop
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Laptop,Desktop,Mobile)
class view(ImportExportModelAdmin):
    pass

# @admin.register(Desktop)
# class view(ImportExportModelAdmin):
#     pass
# @admin.register(Mobile)
# class view(ImportExportModelAdmin):
#     pass

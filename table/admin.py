from django.contrib import admin
from table.models import Field, FilePath


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'width', 'serial_number')


@admin.register(FilePath)
class FilePathAdmin(admin.ModelAdmin):
    list_display = ('path',)
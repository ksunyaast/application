from django.db import models
from django.conf import settings
import os


class Field(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    width = models.PositiveIntegerField(verbose_name='Ширина')
    serial_number = models.PositiveIntegerField(verbose_name='Порядковый номер')


class FilePath(models.Model):
    path = models.TextField()

    @staticmethod
    def get_path():
        file_path = FilePath.objects.first()
        if file_path:
            return file_path.path
        else:
            return None

    @staticmethod
    def set_path(csv_file):
        csv_filepath = os.path.join(settings.BASE_DIR, csv_file)
        values_for_update = {'path': csv_filepath}
        FilePath.objects.update_or_create(id=1, defaults=values_for_update)

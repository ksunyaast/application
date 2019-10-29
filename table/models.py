from django.db import models
from django.conf import settings
from os import path


class Field(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    width = models.PositiveIntegerField(verbose_name='Ширина')
    serial_number = models.PositiveIntegerField(verbose_name='Порядковый номер')


class FilePath(models.Model):
    path = models.TextField()

    @staticmethod
    def get_path():
        file_path = FilePath.objects.all()
        if len(file_path) > 0:
            return file_path[0].path
        else:
            return 'Таблица пуста'

    @staticmethod
    def set_path(csv_file):
        csv_filepath = settings.BASE_DIR + '\\' + csv_file
        file_path = FilePath.objects.all()
        if len(file_path) > 0:
            if file_path[0].path != csv_filepath:
                file_path[0].path = csv_filepath
                file_path[0].save()
        else:
            FilePath.objects.create(path=csv_filepath)

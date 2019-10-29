# Generated by Django 2.1.5 on 2019-10-29 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('width', models.PositiveIntegerField(verbose_name='Ширина')),
                ('serial_number', models.PositiveIntegerField(verbose_name='Порядковый номер')),
            ],
        ),
        migrations.CreateModel(
            name='FilePath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.TextField()),
            ],
        ),
    ]

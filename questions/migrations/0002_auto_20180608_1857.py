# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-08 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_url', models.CharField(default=True, max_length=255)),
                ('url', models.CharField(default=True, max_length=255)),
                ('title', models.CharField(default=True, max_length=255)),
                ('description', models.CharField(default=True, max_length=255)),
                ('title_unique', models.CharField(default=True, max_length=255)),
                ('description_unique', models.CharField(default=True, max_length=255)),
                ('keywords', models.CharField(default=True, max_length=255)),
                ('yandex', models.CharField(default=True, max_length=255)),
                ('google', models.CharField(default=True, max_length=255)),
                ('h1', models.CharField(default=True, max_length=255)),
                ('h2', models.CharField(default=True, max_length=255)),
                ('vk', models.CharField(default=True, max_length=255)),
                ('facebook', models.CharField(default=True, max_length=255)),
                ('instagram', models.CharField(default=True, max_length=255)),
                ('date_add', models.DateField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Description',
        ),
        migrations.DeleteModel(
            name='Googleadwords',
        ),
        migrations.DeleteModel(
            name='H1',
        ),
        migrations.DeleteModel(
            name='H2',
        ),
        migrations.DeleteModel(
            name='H3',
        ),
        migrations.DeleteModel(
            name='H4',
        ),
        migrations.DeleteModel(
            name='H5',
        ),
        migrations.DeleteModel(
            name='Keywords',
        ),
        migrations.DeleteModel(
            name='Title',
        ),
        migrations.DeleteModel(
            name='YandexMetricks',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 08:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('css', '0002_auto_20170203_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='CUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.CharField(max_length=32, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=32)),
                ('last_name', models.CharField(blank=True, max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('user_type', models.CharField(max_length=16)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='FacultyWorkInfo',
            new_name='WorkInfo',
        ),
        migrations.RemoveField(
            model_name='facultydetails',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='sectiontype',
            name='id',
        ),
        migrations.AddField(
            model_name='facultydetails',
            name='user',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='section',
            name='faculty',
            field=models.ForeignKey(default=django.db.models.deletion.SET_NULL, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sectiontype',
            name='section_type',
            field=models.CharField(max_length=32, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]

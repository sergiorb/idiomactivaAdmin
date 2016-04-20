# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 11:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adult',
            options={'verbose_name': 'Adult', 'verbose_name_plural': 'Adults'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
        migrations.RemoveField(
            model_name='adult',
            name='age',
        ),
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
        migrations.AddField(
            model_name='adult',
            name='born_date',
            field=models.DateField(null=True, verbose_name='date of birth'),
        ),
        migrations.AddField(
            model_name='adult',
            name='mobile',
            field=models.CharField(blank=True, max_length=140, null=True, verbose_name='mobile'),
        ),
        migrations.AddField(
            model_name='student',
            name='born_date',
            field=models.DateField(null=True, verbose_name='date of birth'),
        ),
        migrations.AddField(
            model_name='student',
            name='mobile',
            field=models.CharField(blank=True, max_length=140, null=True, verbose_name='mobile'),
        ),
        migrations.AlterField(
            model_name='adult',
            name='added_on',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='added on'),
        ),
        migrations.AlterField(
            model_name='adult',
            name='address',
            field=models.CharField(max_length=140, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='adult',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='adult',
            name='info',
            field=models.TextField(blank=True, null=True, verbose_name='info'),
        ),
        migrations.AlterField(
            model_name='adult',
            name='name',
            field=models.CharField(max_length=140, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='adult',
            name='phone',
            field=models.CharField(blank=True, max_length=140, null=True, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='adult',
            name='surname_a',
            field=models.CharField(max_length=140, verbose_name='surname'),
        ),
        migrations.AlterField(
            model_name='adult',
            name='surname_b',
            field=models.CharField(blank=True, max_length=140, null=True, verbose_name='surname b'),
        ),
        migrations.AlterField(
            model_name='student',
            name='added_on',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='added on'),
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=140, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='student',
            name='adults',
            field=models.ManyToManyField(blank=True, null=True, related_name='students', to='students.Adult', verbose_name='adults'),
        ),
        migrations.AlterField(
            model_name='student',
            name='classes',
            field=models.ManyToManyField(blank=True, null=True, related_name='students', to='classes.Class', verbose_name='classes'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='student',
            name='info',
            field=models.TextField(blank=True, null=True, verbose_name='info'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=140, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=140, null=True, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='schools.School', verbose_name='school'),
        ),
        migrations.AlterField(
            model_name='student',
            name='surname_a',
            field=models.CharField(max_length=140, verbose_name='surname'),
        ),
        migrations.AlterField(
            model_name='student',
            name='surname_b',
            field=models.CharField(blank=True, max_length=140, null=True, verbose_name='surname b'),
        ),
    ]
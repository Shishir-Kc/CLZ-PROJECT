# Generated by Django 5.2.1 on 2025-06-19 08:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_class', '0010_alter_class_class_image'),
        ('teacher', '0008_alter_teacher_teacher_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('1', 'Sunday'), ('2', 'Monday'), ('3', 'Tuesday'), ('4', 'Wednesday'), ('5', 'Thursday'), ('6', 'Friday')], verbose_name='day')),
                ('time', models.CharField(verbose_name='time')),
                ('Class', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='data_class.class', verbose_name='teacher_class')),
                ('Subject', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='data_class.subject', verbose_name='subject')),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher', verbose_name='teacher')),
            ],
            options={
                'verbose_name_plural': 'Schedule',
            },
        ),
    ]

# Generated by Django 5.2.1 on 2025-06-17 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_class', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='faculty',
            field=models.CharField(default='N/A', max_length=30, verbose_name='Faculty'),
        ),
    ]

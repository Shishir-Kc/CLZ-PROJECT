# Generated by Django 5.2.1 on 2025-06-17 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0023_alter_galleryimage_category_alter_news_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievements',
            name='Faculty',
            field=models.IntegerField(default=0, verbose_name='Number of Faculty`s'),
        ),
        migrations.AlterField(
            model_name='achievements',
            name='experience',
            field=models.IntegerField(verbose_name='experience'),
        ),
        migrations.AlterField(
            model_name='achievements',
            name='student',
            field=models.IntegerField(verbose_name='No of Students '),
        ),
        migrations.AlterField(
            model_name='achievements',
            name='sucess_rate',
            field=models.IntegerField(verbose_name='Sucess_rate'),
        ),
        migrations.AlterField(
            model_name='achievements',
            name='teacher',
            field=models.IntegerField(verbose_name='No of Teachers'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact',
            field=models.IntegerField(verbose_name='applicant_contact'),
        ),
    ]

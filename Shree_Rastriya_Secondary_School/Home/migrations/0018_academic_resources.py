# Generated by Django 5.2.1 on 2025-06-15 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0017_alter_head_faculty_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Academic_resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Catalogs', models.FileField(upload_to='pdf/')),
                ('Academic_Policies', models.FileField(upload_to='pdf/')),
                ('Study_Guides', models.FileField(upload_to='pdf/')),
                ('Academic_Calendar', models.FileField(upload_to='pdf/')),
            ],
        ),
    ]

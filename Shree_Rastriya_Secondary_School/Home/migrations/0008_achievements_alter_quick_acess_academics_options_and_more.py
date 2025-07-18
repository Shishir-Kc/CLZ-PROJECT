# Generated by Django 5.2.1 on 2025-06-14 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_quick_acess_academics_quick_acess_admission_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.IntegerField(max_length=1000, verbose_name='No of Students ')),
                ('teacher', models.IntegerField(max_length=1000, verbose_name='No of Teachers')),
                ('experience', models.IntegerField(max_length=100, verbose_name='experience')),
                ('sucess_rate', models.IntegerField(max_length=100, verbose_name='Sucess_rate')),
            ],
        ),
        migrations.AlterModelOptions(
            name='quick_acess_academics',
            options={'verbose_name_plural': 'Quick_Acess_academics'},
        ),
        migrations.AlterModelOptions(
            name='quick_acess_admission',
            options={'verbose_name_plural': 'Quick_Acess_admisison'},
        ),
    ]

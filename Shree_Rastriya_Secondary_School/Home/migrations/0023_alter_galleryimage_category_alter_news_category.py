# Generated by Django 5.2.1 on 2025-06-17 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0022_alter_galleryimage_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='category',
            field=models.CharField(choices=[('Events', 'Events'), ('Activities', 'Activities'), ('Achievements', 'Achievements'), ('Sports', 'Sports'), ('Cultural', 'Cultural')], default='Activities'),
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.CharField(choices=[('Academics', 'Academics'), ('Events', 'Events'), ('Student Life', 'Student Life'), ('Sports', 'Sports'), ('Announcements', 'Announcements'), ('Notice', 'Notice')], default='School News', max_length=100),
        ),
    ]

# Generated by Django 5.2.1 on 2025-06-25 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0025_alter_galleryimage_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='category',
            field=models.CharField(choices=[('Events', 'Events'), ('Activities', 'Activities'), ('Achievements', 'Achievements'), ('Sports', 'Sports'), ('Student Life', 'Student Life'), ('Academics', 'Academics')], default='Activities'),
        ),
    ]

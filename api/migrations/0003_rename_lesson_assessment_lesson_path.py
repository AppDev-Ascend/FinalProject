# Generated by Django 4.2.7 on 2024-01-16 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_section_description_section_length'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assessment',
            old_name='lesson',
            new_name='lesson_path',
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-06 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0005_auto_20201005_2227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appearance',
            old_name='section_background_type',
            new_name='navbar_background_type',
        ),
    ]

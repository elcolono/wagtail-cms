# Generated by Django 3.1.2 on 2020-10-06 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0006_auto_20201006_0521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appearance',
            name='navbar_background_active',
        ),
    ]

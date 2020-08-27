# Generated by Django 3.0.9 on 2020-08-26 21:02

from django.db import migrations
import wagtail_color_panel.fields


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0003_socialmediasettings_header_background_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediasettings',
            name='header_background_color',
            field=wagtail_color_panel.fields.ColorField(blank=True, help_text='Choose background color', max_length=7, null=True),
        ),
    ]
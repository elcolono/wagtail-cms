# Generated by Django 3.0.9 on 2020-08-30 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0003_layout'),
    ]

    operations = [
        migrations.AddField(
            model_name='layout',
            name='bad',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]

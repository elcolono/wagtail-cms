# Generated by Django 3.0.10 on 2020-09-06 08:32

from django.db import migrations, models
import section.models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0005_auto_20200906_0751'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyMixinModelTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myfield', section.models.MyMixinCharField(max_length=512, new_arg='myarg')),
            ],
        ),
    ]

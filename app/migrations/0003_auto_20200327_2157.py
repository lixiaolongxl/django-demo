# Generated by Django 2.1 on 2020-03-27 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200327_2140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='areainfo',
            old_name='aParent_id',
            new_name='aParent',
        ),
    ]

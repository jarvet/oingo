# Generated by Django 2.1.4 on 2018-12-13 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oingo', '0003_auto_20181212_0234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filter',
            old_name='tname',
            new_name='tag',
        ),
    ]

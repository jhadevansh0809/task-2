# Generated by Django 4.2 on 2023-04-23 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_permission'),
    ]

    operations = [
        migrations.RenameField(
            model_name='permission',
            old_name='permission_level',
            new_name='access_level',
        ),
    ]

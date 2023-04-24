# Generated by Django 4.2 on 2023-04-23 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_permission_level_permission_access_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permission',
            name='organisation',
        ),
        migrations.AddField(
            model_name='permission',
            name='organisation',
            field=models.ManyToManyField(to='api.organisation'),
        ),
    ]

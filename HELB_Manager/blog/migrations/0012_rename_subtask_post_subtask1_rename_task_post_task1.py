# Generated by Django 4.1.2 on 2023-01-01 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_rename_subtask1_post_subtask_rename_task1_post_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='subtask',
            new_name='subtask1',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='task',
            new_name='task1',
        ),
    ]

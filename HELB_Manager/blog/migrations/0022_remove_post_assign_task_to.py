# Generated by Django 4.1.2 on 2023-01-05 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_post_assign_task_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='assign_task_to',
        ),
    ]

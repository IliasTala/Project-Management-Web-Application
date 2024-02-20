# Generated by Django 4.1.2 on 2023-01-03 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_delete_draggablestate_delete_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='subtask1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='subtask2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='subtask3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='task1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='task2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='task3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='task4',
        ),
        migrations.RemoveField(
            model_name='post',
            name='task5',
        ),
        migrations.RemoveField(
            model_name='post',
            name='task6',
        ),
        migrations.AddField(
            model_name='post',
            name='tasks',
            field=models.TextField(default='exit', max_length=100),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.1.2 on 2023-01-02 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_rename_subtask_post_subtask1_rename_task_post_task1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='status',
            new_name='status1',
        ),
        migrations.AddField(
            model_name='post',
            name='status2',
            field=models.TextField(default='exit', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='status3',
            field=models.TextField(default='exit', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='status4',
            field=models.TextField(default='exit', max_length=100),
            preserve_default=False,
        ),
    ]
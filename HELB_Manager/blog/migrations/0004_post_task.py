# Generated by Django 4.1.2 on 2022-11-28 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_task_subtask'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='task',
            field=models.CharField(default='exit', max_length=100),
            preserve_default=False,
        ),
    ]
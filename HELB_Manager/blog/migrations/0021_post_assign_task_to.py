# Generated by Django 4.1.2 on 2023-01-03 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_remove_post_contributor_post_contributor'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='assign_task_to',
            field=models.TextField(default='contrib2'),
            preserve_default=False,
        ),
    ]
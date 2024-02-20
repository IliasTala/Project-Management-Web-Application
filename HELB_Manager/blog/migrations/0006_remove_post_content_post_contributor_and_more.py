# Generated by Django 4.1.2 on 2022-12-19 16:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_rename_subtask_post_subtask1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='contributor',
            field=models.ManyToManyField(related_name='contributor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(max_length=100),
        ),
    ]

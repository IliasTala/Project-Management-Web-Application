# Generated by Django 4.1.2 on 2022-12-31 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_draggablestate_delete_subtask'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='draggablestate',
            name='modified_at',
        ),
    ]
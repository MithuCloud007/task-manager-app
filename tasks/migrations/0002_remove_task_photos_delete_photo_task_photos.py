# Generated by Django 5.0.1 on 2024-01-30 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='photos',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.AddField(
            model_name='task',
            name='photos',
            field=models.FileField(blank=True, null=True, upload_to='tasks/task'),
        ),
    ]

# Generated by Django 4.2.20 on 2025-03-21 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='list',
            new_name='lista',
        ),
        migrations.AddField(
            model_name='task',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

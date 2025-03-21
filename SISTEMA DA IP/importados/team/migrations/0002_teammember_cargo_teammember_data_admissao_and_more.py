# Generated by Django 4.2.20 on 2025-03-20 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='cargo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='data_admissao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='departamento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='observacoes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='telefone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

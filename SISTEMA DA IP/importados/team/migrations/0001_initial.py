# Generated by Django 4.2.20 on 2025-03-19 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_avaliacao', models.CharField(choices=[('semanal', 'Semanal'), ('mensal', 'Mensal')], max_length=10)),
                ('nota', models.IntegerField(help_text='Avaliação de 1 a 5')),
                ('comentario', models.TextField(blank=True, null=True)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluations', to='reports.report')),
                ('team_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluations', to='team.teammember')),
            ],
        ),
    ]

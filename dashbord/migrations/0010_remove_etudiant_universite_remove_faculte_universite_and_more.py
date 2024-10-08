# Generated by Django 4.0.4 on 2024-07-11 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashbord', '0009_alter_stage_date_debut_alter_stage_date_fin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiant',
            name='Universite',
        ),
        migrations.RemoveField(
            model_name='faculte',
            name='universite',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='universite',
        ),
        migrations.RemoveField(
            model_name='user',
            name='universite',
        ),
        migrations.AddField(
            model_name='faculte',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stage',
            name='faculte',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashbord.faculte'),
        ),
        migrations.AddField(
            model_name='user',
            name='faculte',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashbord.faculte'),
        ),
        migrations.AlterField(
            model_name='entreprise',
            name='nom',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='faculte',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashbord.faculte'),
        ),
        migrations.AlterField(
            model_name='universite',
            name='nom',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]

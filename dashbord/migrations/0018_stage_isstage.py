# Generated by Django 4.0.4 on 2024-07-11 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashbord', '0017_alter_entreprise_nom_alter_faculte_nom'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='isStage',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 5.0.1 on 2024-07-03 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashbord', '0004_alter_etudiant_faculte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='date_debut',
            field=models.DateField(auto_created=True),
        ),
    ]

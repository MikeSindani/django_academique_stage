# Generated by Django 4.0.4 on 2024-07-11 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashbord', '0012_alter_universite_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entreprise',
            name='nom',
            field=models.CharField(max_length=200),
        ),
    ]

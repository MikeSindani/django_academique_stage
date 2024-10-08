# Generated by Django 4.0.4 on 2024-07-18 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashbord', '0019_stage_date_inscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('faculte', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashbord.faculte')),
            ],
        ),
    ]

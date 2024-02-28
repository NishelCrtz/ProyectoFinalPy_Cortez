# Generated by Django 5.0.1 on 2024-02-04 08:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coffee_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asociado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puesto', models.TextField()),
                ('calificacion', models.IntegerField()),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Coffee_app.cliente')),
            ],
        ),
        migrations.DeleteModel(
            name='Resena',
        ),
    ]

# Generated by Django 5.0.1 on 2024-02-25 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coffee_app', '0008_alter_asociado_calificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bebida',
            name='descripcion',
            field=models.CharField(max_length=100),
        ),
    ]

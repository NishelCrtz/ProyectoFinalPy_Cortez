# Generated by Django 5.0.1 on 2024-02-05 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coffee_app', '0003_alter_asociado_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.IntegerField(max_length=15),
        ),
    ]
# Generated by Django 5.0.1 on 2024-02-25 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coffee_app', '0009_alter_bebida_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bebida',
            name='descripcion',
            field=models.TextField(),
        ),
    ]
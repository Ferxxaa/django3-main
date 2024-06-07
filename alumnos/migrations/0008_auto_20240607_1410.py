# Generated by Django 3.2.12 on 2024-06-07 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0007_alter_alumnoseccion_id_alumno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='activo',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='apellido_materno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='apellido_paterno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='id_genero',
            field=models.ForeignKey(db_column='idGenero', null=True, on_delete=django.db.models.deletion.CASCADE, to='alumnos.genero'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='telefono',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
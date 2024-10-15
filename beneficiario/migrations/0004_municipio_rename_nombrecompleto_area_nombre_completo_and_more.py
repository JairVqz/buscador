# Generated by Django 4.1.13 on 2024-10-14 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiario', '0003_alter_area_table_alter_programa_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cve_edo', models.IntegerField(max_length=10)),
                ('cve_mpio', models.IntegerField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('territorio', models.IntegerField(max_length=100)),
            ],
            options={
                'db_table': 'municipios',
            },
        ),
        migrations.RenameField(
            model_name='area',
            old_name='nombreCompleto',
            new_name='nombre_completo',
        ),
        migrations.RenameField(
            model_name='beneficiario',
            old_name='apellidoMaterno',
            new_name='apellido_materno',
        ),
        migrations.RenameField(
            model_name='beneficiario',
            old_name='apellidoPaterno',
            new_name='apellido_paterno',
        ),
        migrations.DeleteModel(
            name='Programa',
        ),
    ]

# Generated by Django 5.2 on 2025-04-09 14:35

import colorfield.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaracteristicaMedicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('unidad_medida', models.CharField(max_length=20)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaPuntoMedicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_equipo', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UbicacionTecnica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_ubicacion', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InterfaceConsumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('consumo', models.FloatField()),
                ('medidor', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'interface_core_consumo',
                'managed': True,
                'unique_together': {('fecha', 'medidor')},
            },
        ),
        migrations.CreateModel(
            name='PuntoMedicion',
            fields=[
                ('numero_interno', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=255)),
                ('es_contador', models.BooleanField(default=False, verbose_name='Es Contador')),
                ('caracteristica', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.caracteristicamedicion')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.categoriapuntomedicion')),
                ('objeto_tecnico_equipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.equipo', verbose_name='Equipo Asociado')),
                ('objeto_tecnico_ubicacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.ubicaciontecnica', verbose_name='Ubicación Técnica Asociada')),
            ],
            options={
                'verbose_name': 'Punto de Medición',
                'verbose_name_plural': 'Puntos de Medición',
            },
        ),
        migrations.CreateModel(
            name='DocumentoMedicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora_lectura', models.DateTimeField(verbose_name='Fecha y hora de lectura')),
                ('valor_leido', models.FloatField()),
                ('lectura_contador', models.FloatField(blank=True, null=True, verbose_name='Lectura de Contador (si aplica)')),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('punto_medicion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.puntomedicion')),
            ],
            options={
                'verbose_name': 'Documento de Medición',
                'verbose_name_plural': 'Documentos de Medición',
                'ordering': ['-fecha_hora_lectura'],
            },
        ),
        migrations.CreateModel(
            name='RangoMedicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_min', models.FloatField(verbose_name='Valor mínimo')),
                ('valor_max', models.FloatField(verbose_name='Valor máximo')),
                ('descripcion', models.CharField(max_length=255, verbose_name='Descripción')),
                ('color', colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=25, samples=None, verbose_name='Color representativo')),
                ('caracteristica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rangos', to='core.caracteristicamedicion')),
            ],
            options={
                'verbose_name': 'Rango de Medición',
                'verbose_name_plural': 'Rangos de Medición',
                'ordering': ['caracteristica', 'valor_min'],
            },
        ),
        migrations.CreateModel(
            name='Consumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('consumo', models.FloatField(blank=True, null=True)),
                ('medidor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consumos', to='core.medidor')),
            ],
            options={
                'verbose_name': 'Consumo',
                'verbose_name_plural': 'Consumos',
                'unique_together': {('fecha', 'medidor')},
            },
        ),
    ]

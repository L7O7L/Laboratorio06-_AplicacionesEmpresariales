# Generated by Django 4.1.1 on 2022-09-27 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('RentaPeliculas', '0009_remove_rentas_pelicula_rentada_remove_rentas_usuario_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('genero', models.CharField(max_length=200, verbose_name='Género')),
                ('director', models.CharField(max_length=200, verbose_name='Director')),
                ('duracion', models.TimeField(verbose_name='Duración')),
                ('fecha_publicacion', models.DateField(verbose_name='Fecha de Publicación')),
            ],
            options={
                'verbose_name': 'Pelicula',
                'verbose_name_plural': 'Peliculas',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=200, verbose_name='Apellido')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('fecha_registro', models.DateTimeField(verbose_name='Fecha de Registro')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Email')),
                ('dni', models.CharField(blank=True, max_length=8, null=True, verbose_name='DNI')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='Renta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_renta', models.DateTimeField(verbose_name='Fecha de la Renta')),
                ('pelicula_rentada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RentaPeliculas.pelicula')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RentaPeliculas.usuario')),
            ],
            options={
                'verbose_name': 'Renta',
                'verbose_name_plural': 'Rentas',
            },
        ),
    ]

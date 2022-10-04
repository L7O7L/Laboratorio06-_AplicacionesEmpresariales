from django.db import models

# Create your models here.

class Nacionalidad(models.Model):

    id = models.AutoField(primary_key=True)
    nacionalidad = models.CharField(max_length = 100)

    class Meta:

        verbose_name = "Nacionalidad"
        verbose_name_plural = "Nacionalidades"

    def __str__(self):

        return self.nacionalidad

class Director(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento')
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)

    class Meta: 

        verbose_name = "Director"
        verbose_name_plural = "Directores"
    
    def __str__(self):

        return self.apellidos + ', ' + self.nombre

class Actor(models.Model): 

    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=200)
    apellido = models.CharField('Apellido', max_length=200)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento')
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    
    class Meta: 

        verbose_name = "Actor"
        verbose_name_plural = "Actores"

    def __str__(self):
        return self.apellido + ', ' + self.nombre

class Personaje(models.Model):

    name_role = models.CharField('Nombre', max_length=100)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    

    class Meta:

        verbose_name = "Personaje"
        verbose_name_plural = "Personajes"

    def __str__(self):
        return self.name_role

class Categoria(models.Model):

    categoria = models.CharField('Categoria', max_length=50)

    class Meta:

        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.categoria

class Genero(models.Model):

    genero = models.CharField('Genero', max_length=50)

    class Meta:

        verbose_name = "Genero"
        verbose_name_plural = "Géneros"

    def __str__(self):
        return self.genero

class Pelicula(models.Model):

    nombre = models.CharField('Nombre', max_length=200, null=False)
    duracion = models.TimeField('Duración', null=False)
    genero = models.ManyToManyField(Genero)
    director = models.ManyToManyField(Director)
    personajes_principales = models.ManyToManyField(Personaje)
    categoria = models.ManyToManyField(Categoria) 
    fecha_publicacion = models.DateField('Fecha de Publicación', null=False)

    def get_genero(self):
        return ", ".join([p.genero for p in self.genero.all()])
    
    def get_director(self):
        return ", ".join([e.nombre for e in self.director.all()])
    
    def get_personajes_principales(self):
        return ", ".join([i.name_role for i in self.personajes_principales.all()])

    def get_categoria(self):
        return ", ".join([i.categoria for i in self.categoria.all()])

    class Meta:

        verbose_name = "Pelicula"
        verbose_name_plural = "Peliculas"
        ordering = ['fecha_publicacion']

    def __str__(self):
        return self.nombre

class Usuario(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=200, null=False)
    apellido = models.CharField('Apellido', max_length=200, null=False)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento', null=False)
    fecha_registro = models.DateTimeField('Fecha de Registro', null=False)
    email = models.EmailField('Email', max_length=200, blank=True, null=True)
    dni = models.CharField('DNI', max_length=8, blank=True, null=True, unique=True)

    class Meta:

        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['apellido']

    def __str__(self):
        return self.apellido + ', ' + self.nombre

class Renta(models.Model):

    id = models.AutoField(primary_key=True)
    pelicula_rentada = models.ForeignKey(Pelicula, on_delete=models.CASCADE, null=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
    fecha_renta = models.DateTimeField('Fecha de la Renta', null=False)

    class Meta:

        verbose_name = "Renta"
        verbose_name_plural = "Rentas"
        ordering = ['id']

    def __str__(self):
        return 'N° de Renta ' + str(self.id) + ' --> ' + ' IdUser:  ' + str(self.usuario.id)

from django.contrib import admin
from .models import Usuario, Pelicula, Renta, Actor, Categoria, Genero, Nacionalidad, Director, Personaje

class ListaPersonajes(admin.ModelAdmin):

    list_display = ("name_role", "actor")
    search_fields = ("name_role", "actor__nombre", "actor__apellido",)

class ListaDirectores(admin.ModelAdmin):

    list_display = ("nombre", "apellidos", "nacionalidad", "fecha_nacimiento")
    search_fields = ("nombre", "apellidos")
    date_hierarchy = "fecha_nacimiento"

class ListaActores(admin.ModelAdmin):

    list_display = ("nombre", "apellido", "nacionalidad", "fecha_nacimiento")
    search_fields = ("nombre", "apellido",)
    date_hierarchy = "fecha_nacimiento"

class ListaUsuarios(admin.ModelAdmin):

    #Ordenarlo en formato de tablas
    list_display = ("id" ,"nombre" ,"apellido" ,"email" ,"dni" ,"fecha_registro")

    date_hierarchy = "fecha_registro"
    list_filter = ("fecha_registro",)

    #Casilla de búsqueda
    search_fields = ("nombre", "apellido", "dni")

class ListaRenta(admin.ModelAdmin):

    list_display = ("id", "usuario", "pelicula_rentada", "fecha_renta")
    search_fields = ("pelicula_rentada__nombre", "usuario__apellido", "usuario__nombre")
    list_filter = ("fecha_renta",)
    date_hierarchy = "fecha_renta"

class ListaPeliculas(admin.ModelAdmin):

    list_display = ("nombre", "get_director", "get_personajes_principales", "get_genero", "get_categoria", "fecha_publicacion")
    search_fields = ("nombre", "director__nombre")
    list_filter = ("genero", "categoria")
    date_hierarchy = "fecha_publicacion"

# Register your models here.

admin.site.register(Pelicula, ListaPeliculas)
admin.site.register(Usuario, ListaUsuarios)
admin.site.register(Renta, ListaRenta)
admin.site.register(Actor, ListaActores)
admin.site.register(Categoria)
admin.site.register(Genero)
admin.site.register(Nacionalidad)
admin.site.register(Director, ListaDirectores)
admin.site.register(Personaje, ListaPersonajes)


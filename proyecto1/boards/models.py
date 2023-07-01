from django.db import models  #nos da indicios de que estaremos trabajando con BD


# Create your models here.

class Boards(models.Model):
    id = models.AutoField(primary_key=True) #uuid vamos a generar un INT
    titulo= models.CharField(max_length=200)
    descripcion = models.TextField()
    #buenapractica
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'tablero'
        verbose_name_plural = 'Tableros'
        permissions = (("es_miembro_1","Es miembro con prioridad 1"),)#por si queremos crear mas de un permiso

    def __str__(self):
        return self.titulo


TITLE_CHOICES = [
    ('MR','Mr.'),
    ('MRS','Mrs.'),
    ('MS','Ms.'),
]
class Author(models.Model):
    id = models.AutoField(primary_key=True) #uuid vamos a generar un INT
    name = models.CharField(max_length=100, verbose_name='Nombre')
    title = models.CharField(max_length=3, choices=TITLE_CHOICES, verbose_name='Titulo')
    birth_date = models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')
    #buenas practicas
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        verbose_name = 'autor'
        verbose_name_plural = 'Autores'
        ordering = ['created']

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True) #uuid vamos a generar un INT
    name = models.CharField(max_length=100, verbose_name='Nombre')
    authors = models.ManyToManyField(Author, verbose_name='Autor(es)')
    #buenas practicas
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.name

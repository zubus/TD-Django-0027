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
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)
    #buenas practicas
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True) #uuid vamos a generar un INT
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    #buenas practicas
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



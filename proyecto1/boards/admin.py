from django.contrib import admin, messages

from .models import Author, Boards, Book

# Register your models here.

""" recomendado pildoras informaticas curso Django(panel administrador I, II, III, etc) https://www.youtube.com/watch?v=wwAcsIW86UQ   
UZko...  panel admin     https://www.youtube.com/watch?v=i_Zq2LUb5zE
"""

admin.site.site_header = 'Curso Django'
admin.site.index_title = 'Panel de control Proyecto Django'
admin.site.site_title = 'Administrador Django'

class OnlyReadAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']

class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']
    list_display = ('title','name', 'birth_date')
    search_fields= ('name',)
    list_filter = ('name', 'birth_date')

def actualizar_nombre(modeladmin, request,queryset):
    queryset.update(name='Chupacabra')
    messages.success(request, "Nombre actualizado")


    
admin.site.add_action(actualizar_nombre, "actualizar a chupacabra")
admin.site.register(Book, OnlyReadAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Boards, OnlyReadAdmin)
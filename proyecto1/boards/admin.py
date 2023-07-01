from django.contrib import admin
from .models import Book,Author,Boards
# Register your models here.


admin.site.site_header = 'Curso Django'
admin.site.index_title = 'Panel de control Proyecto Django'
admin.site.site_title = 'Administrador Django'
class OnlyReadAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']

class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']
    list_display = ('title','name', 'birth_date')
    search_fields= ('name',)
    

admin.site.register(Book, OnlyReadAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Boards, OnlyReadAdmin)
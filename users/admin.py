"""User admin classes"""
#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#models
from users.models import *
from posts.models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin"""
    #hace ver los campos que yo quiera en el modelo de user
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    #crea links de acceso en los mismos campos
    list_display_links = ('user', 'picture')
    #editable en la tabla
    list_editable = ('website', 'phone_number')
    #busqueda por campos
    search_fields = (
        'user__email',
        'user__first_name'

    )
    #filtros establecidos por campos
    list_filter = (
        'created',
        'modified',
        'user__is_active',
    )
    #editar visualización de detalle 
    #tupla titulo con diccionario de fields que pueden ser
    #tuplas dependiendo de ubicación
    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'picture'),
            )
        }),
        ('Extra Info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography'),
            )
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified'),
              
            )
        }),
    )
    #campos que no se pueden modificar
    readonly_fields=('created','modified')
class ProfileInLine(admin.StackedInline):
    """Profile inline admin for users"""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines=(ProfileInLine,)
    

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Post)
    

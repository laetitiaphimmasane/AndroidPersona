from django.contrib import admin
from .models import Persona


class PersonaAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name', 'address_street','address_number', 'email']
    list_filter=['age','city']


admin.site.register(Persona, PersonaAdmin)

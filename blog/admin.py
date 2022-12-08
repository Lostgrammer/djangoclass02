from django.contrib import admin

# Registrar modelos creados aca
from .models import Laptop,Refri

admin.site.register(Refri)
admin.site.register(Laptop)

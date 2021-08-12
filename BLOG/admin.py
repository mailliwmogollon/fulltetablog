from django.contrib import admin
from .models import Producto, Salud, Motricidad, Rincon

# Register your models here.
admin.site.register(Producto)
admin.site.register(Salud)
admin.site.register(Motricidad)
admin.site.register(Rincon)
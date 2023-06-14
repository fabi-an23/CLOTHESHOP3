from django.contrib import admin
from .models import Marca, Producto, Contacto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "nuevo", "marca"]
    search_fields = ["nombre"]
    list_per_page = 5

admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)
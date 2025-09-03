from django.contrib import admin
from .models import Order_Model, Order_Item
# Register your models here.


class OrderItemInline(admin.TabularInline):
    model = Order_Item
    raw_id_fields = ['PRODUCT']


@admin.register(Order_Model)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "nombre_completo", "correo", "direccion",
        "fecha_creacion", "fecha_actualizacion", "total_cost", "pagado"
    ]
    inlines = [OrderItemInline]

    def nombre_completo(self, obj):
        return obj.FULL_NAME
    nombre_completo.short_description = "Nombre Completo"

    def correo(self, obj):
        return obj.EMAIL
    correo.short_description = "Correo Electrónico"

    def direccion(self, obj):
        return obj.ADDRESS
    direccion.short_description = "Dirección"

    def fecha_creacion(self, obj):
        return obj.CREATED_AT
    fecha_creacion.short_description = "Fecha de Creación"

    def fecha_actualizacion(self, obj):
        return obj.UPDATED_AT
    fecha_actualizacion.short_description = "Fecha de Actualización"

    def pagado(self, obj):
        return obj.PAID
    pagado.short_description = "Pagado"
    pagado.boolean = True

    def total_cost(self, obj):
        return f"${obj.get_total_cost():.2f}"
    total_cost.short_description = "Total"

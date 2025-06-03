from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "nombre_completo", "correo", "direccion",
        "fecha_creacion", "fecha_actualizacion", "total_cost", "pagado"
    ]
    inlines = [OrderItemInline]
    
    def nombre_completo(self, obj):
        return obj.full_name
    nombre_completo.short_description = "Nombre Completo"

    def correo(self, obj):
        return obj.email
    correo.short_description = "Correo Electrónico"

    def direccion(self, obj):
        return obj.address
    direccion.short_description = "Dirección"

    def fecha_creacion(self, obj):
        return obj.created_at
    fecha_creacion.short_description = "Fecha de Creación"

    def fecha_actualizacion(self, obj):
        return obj.updated_at
    fecha_actualizacion.short_description = "Fecha de Actualización"
    
    def pagado(self, obj):
        return obj.paid
    pagado.short_description = "Pagado"
    pagado.boolean = True

    def total_cost(self, obj):
        return f"${obj.get_total_cost():.2f}"
    total_cost.short_description = "Total"

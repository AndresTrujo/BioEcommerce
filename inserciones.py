import os
import django
from django.utils import timezone
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biocommerce.settings')
django.setup()
from products.models import Producto, Categoria

## Categorias
# 1. Insertar Categorías

def cambiar_estado_producto(clave, activar=True):
    try:
        producto = Producto.objects.get(ID_PRODUCTO=clave)
        producto.PROD_ACTIVO = activar
        producto.save()

        # Cambiar el estado en el mensaje
        estado = "activado" if activar else "desactivado"

        # Modificar el nombre del estado si el producto está inactivo
        estado_mostrado = "Activo" if activar else "Inactivo"

        print(f"✅ Producto '{producto.PROD_NOMBRE}' ({clave}) {estado_mostrado} correctamente.")
    except Producto.DoesNotExist:
        print("❌ Producto no encontrado.")


def inserciones():
    ## Categorias
    # 1. Insertar Categorías
    cat1, created = Categoria.objects.get_or_create(CAT_NOMBRE="AMINOACIDOS",CAT_SLUG="aminoacidos")
    cat2, created = Categoria.objects.get_or_create(CAT_NOMBRE="NUTRACEUTICOS", CAT_SLUG="nutraceuticos")
    cat3, created = Categoria.objects.get_or_create(CAT_NOMBRE="ANTIOXIDANTES", CAT_SLUG="antioxidantes")
    cat4, created = Categoria.objects.get_or_create(CAT_NOMBRE="VITAMINAS", CAT_SLUG="vitaminas")
    cat5, created = Categoria.objects.get_or_create(CAT_NOMBRE="MINERALES", CAT_SLUG="minerales")
    cat6, created = Categoria.objects.get_or_create(CAT_NOMBRE="SUPLEMENTOS EN POLVO", CAT_SLUG="suplementos-en-polvo")
    cat7, created = Categoria.objects.get_or_create(CAT_NOMBRE="PROTEINAS", CAT_SLUG="proteinas")
    cat8, created = Categoria.objects.get_or_create(CAT_NOMBRE="COLAGENOS", CAT_SLUG="colagenos")
    cat9, created = Categoria.objects.get_or_create(CAT_NOMBRE="FAT BURNERS", CAT_SLUG="fat-burners")

    # AMINOACIDOS
    prod1, created = Producto.objects.update_or_create(
        ID_PRODUCTO="AM001",
        defaults={
            'PROD_CATEGORIA': cat1,
            'PROD_NOMBRE': "L-ARGININA",
            'CONTENIDO_PZS': "90 piezas",
            'PROD_DESCRIPCION': "Cápsulas",
            'PROD_PRECIO_MAY': 174.00,
            'PROD_PRECIO_PUB': 220.00,
            'PROD_GRAMAJE': 500,
        }
    )
    if created:
        print(f"Producto '{prod1.PROD_NOMBRE}' (AM001) creado.")
    else:
        print(f"Producto '{prod1.PROD_NOMBRE}' (AM001) ya existía. Actualizando gramaje.")
        prod1.PROD_GRAMAJE = 500.00
        prod1.save()
        print(f"Producto '{prod1.PROD_NOMBRE}' (AM001) actualizado con gramaje.")

    prod2, created = Producto.objects.update_or_create(
        ID_PRODUCTO="AM002",
        defaults={
        'PROD_CATEGORIA':cat1,
        'PROD_NOMBRE':"L-ARGININA",
        'CONTENIDO_PZS':"180 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':280.00,
        'PROD_PRECIO_PUB':360.00,
        'PROD_GRAMAJE':500.00,
        }
    )
    if created:
        print(f"Producto '{prod2.PROD_NOMBRE}' (AM002) creado.")
    else:
        print(f"Producto '{prod2.PROD_NOMBRE}' (AM002) ya existía. Actualizando gramaje.")
        prod2.PROD_GRAMAJE = 500.00
        prod2.save()
        print(f"Producto '{prod2.PROD_NOMBRE}' (AM002) actualizado con gramaje.")


    prod3, created = Producto.objects.update_or_create(
        ID_PRODUCTO="AM003",
        defaults={
        'PROD_CATEGORIA':cat1,
        'PROD_NOMBRE':"L-ARGININA",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':210.00,
        'PROD_PRECIO_PUB':260.00,
        'PROD_GRAMAJE':1000.00
         }
    )
    if created:
        print(f"Producto '{prod3.PROD_NOMBRE}' (AM003) creado.")
    else:
        print(f"Producto '{prod3.PROD_NOMBRE}' (AM003) ya existía. Actualizando gramaje.")
        prod3.PROD_GRAMAJE = 1000.00
        prod3.save()
        print(f"Producto '{prod3.PROD_NOMBRE}' (AM003) actualizado con gramaje.")


    prod4, created = Producto.objects.update_or_create(
        ID_PRODUCTO="AM004",
        defaults={
        'PROD_CATEGORIA':cat1,
        'PROD_NOMBRE':"L-ARGININA",
        'CONTENIDO_PZS':"160 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':330.00,
        'PROD_PRECIO_PUB':420.00,
        'PROD_GRAMAJE':1000.00
        }
    )
    if created:
        print(f"Producto '{prod4.PROD_NOMBRE}' (AM004) creado.")
    else:
        print(f"Producto '{prod4.PROD_NOMBRE}' (AM004) ya existía. Actualizando gramaje.")
        prod4.PROD_GRAMAJE = 1000.00
        prod4.save()
        print(f" Producto '{prod4.PROD_NOMBRE}' (AM004) actualizado con gramaje.")

    prod5, created = Producto.objects.update_or_create(
        ID_PRODUCTO="AM005",
        defaults={
        'PROD_CATEGORIA':cat1,
        'PROD_NOMBRE':"CREATINA 5000 PURE NATURAL",
        'CONTENIDO_PZS':"300 GRAMOS",
        'PROD_DESCRIPCION':"POLVO",
        'PROD_PRECIO_MAY':390.00,
        'PROD_PRECIO_PUB':460.00,
        'PROD_GRAMAJE':300.00
    }
    )
    if created:
        print(f"Producto '{prod5.PROD_NOMBRE}' (AM005) creado.")
    else:
        print(f"Producto '{prod5.PROD_NOMBRE}' (AM005) ya existía. Actualizando gramaje.")
        prod5.PROD_GRAMAJE = 300.00
        prod5.save()
        print(f"Producto '{prod5.PROD_NOMBRE}' (AM005) actualizado con gramaje.")

    prod6, created = Producto.objects.update_or_create(
        ID_PRODUCTO="AM006",
        defaults={
        'PROD_CATEGORIA':cat1,
        'PROD_NOMBRE':"CREATINA 5000 TROPICAL FRUITS",
        'CONTENIDO_PZS':"300 GRAMOS",
        'PROD_DESCRIPCION':"POLVO",
        'PROD_PRECIO_MAY':390.00,
        'PROD_PRECIO_PUB':460.00,
        'PROD_GRAMAJE':300.00
        }
    )
    if created:
        print(f"Producto '{prod6.PROD_NOMBRE}' (AM006) creado.")
    else:
        print(f"Producto '{prod6.PROD_NOMBRE}' (AM006) ya existía. Actualizando gramaje.")
        prod6.PROD_GRAMAJE = 300.00
        prod6.save()
        print(f"Producto '{prod6.PROD_NOMBRE}' (AM006) actualizado con gramaje.")
    
    prod7, created = Producto.objects.update_or_create(
        ID_PRODUCTO="AM007",
        defaults={
        'PROD_CATEGORIA':cat1,
        'PROD_NOMBRE':"CREATINA 5000 MANZANA VERDE",
        'CONTENIDO_PZS':"300 GRAMOS",
        'PROD_DESCRIPCION':"POLVO",
        'PROD_PRECIO_MAY':390.00,
        'PROD_PRECIO_PUB':460.00,
        'PROD_GRAMAJE':300.00
        }
    )
    if created:
        print(f"Producto '{prod7.PROD_NOMBRE}' (AM007) creado.")
    else:
        print(f"Producto '{prod7.PROD_NOMBRE}' (AM007) ya existía. Actualizando gramaje.")
        prod7.PROD_GRAMAJE = 300.00
        prod7.save()
        print(f"Producto '{prod7.PROD_NOMBRE}' (AM007) actualizado con gramaje.")
    
    prod8, created = Producto.objects.update_or_create(
        ID_PRODUCTO="AM008",
        defaults={
        'PROD_CATEGORIA':cat1,
        'PROD_NOMBRE':"CREATINA 5000 BERRIES DELICIOUS",
        'CONTENIDO_PZS':"300 GRAMOS",
        'PROD_DESCRIPCION':"POLVO",
        'PROD_PRECIO_MAY':390.00,
        'PROD_PRECIO_PUB':460.00,
        'PROD_GRAMAJE':300.00
        }
    )
    if created:
        print(f"Producto '{prod8.PROD_NOMBRE}' (AM008) creado.")
    else:
        print(f"Producto '{prod8.PROD_NOMBRE}' (AM008) ya existía. Actualizando gramaje.")
        prod8.PROD_GRAMAJE = 300.00
        prod8.save()
        print(f"Producto '{prod8.PROD_NOMBRE}' (AM008) actualizado con gramaje.")
    
    prod9, created = Producto.objects.update_or_create(
        ID_PRODUCTO="AM009",
        defaults={
        'PROD_CATEGORIA':cat1,
        'PROD_NOMBRE':"CREATINA 3000",
        'CONTENIDO_PZS':"90 PIEZAS",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':182.00,
        'PROD_PRECIO_PUB':230.00,
        'PROD_GRAMAJE':3000.00
        }
    )
    if created:
        print(f"Producto '{prod9.PROD_NOMBRE}' (AM009) creado.")
    else:
        print(f"Producto '{prod9.PROD_NOMBRE}' (AM009) ya existía. Actualizando gramaje.")
        prod9.PROD_GRAMAJE = 270.00
        prod9.save()
        print(f"Producto '{prod9.PROD_NOMBRE}' (AM009) actualizado con gramaje.")
    
    prod10, created = Producto.objects.update_or_create(
        ID_PRODUCTO="AM0010",
        defaults={
        'PROD_CATEGORIA':cat1,
        'PROD_NOMBRE':"CREATINA 3000",
        'CONTENIDO_PZS':"160 PIEZAS",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':264.00,
        'PROD_PRECIO_PUB':345.00,
        'PROD_GRAMAJE':480.00
        }
    )
    if created:
        print(f"Producto '{prod10.PROD_NOMBRE}' (AM0010) creado.")
    else:
        print(f"Producto '{prod10.PROD_NOMBRE}' (AM0010) ya existía. Actualizando gramaje.")
        prod10.PROD_GRAMAJE = 480.00
        prod10.save()
        print(f"Producto '{prod10.PROD_NOMBRE}' (AM0010) actualizado con gramaje.")
    
    prod11, created = Producto.objects.update_or_create(
        ID_PRODUCTO="AM0011",
        defaults={
        'PROD_CATEGORIA':cat1,
        'PROD_NOMBRE':"TRIPTOFANO",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':248.00,
        'PROD_PRECIO_PUB':310.00,
        }
    )
    if created:
        print(f"Producto '{prod11.PROD_NOMBRE}' (AM0011) creado sin gramaje.")
    else:
        print(f"Producto '{prod11.PROD_NOMBRE}' (AM0011) ya existía.")
        print(f"Producto '{prod11.PROD_NOMBRE}' (AM0011) no se actualizó el gramaje.")   
    
    prod12, created = Producto.objects.update_or_create(
        ID_PRODUCTO="AM0012",
        defaults={
        'PROD_CATEGORIA':cat1,
        'PROD_NOMBRE':"TRIPTOFANO",
        'CONTENIDO_PZS':"160 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':370.00,
        'PROD_PRECIO_PUB':460.00,
        }
    )
    if created:
        print(f"Producto '{prod12.PROD_NOMBRE}' (AM0012) creado sin gramaje.")
    else:
        print(f"Producto '{prod12.PROD_NOMBRE}' (AM0012) ya existía.")
        print(f"Producto '{prod12.PROD_NOMBRE}' (AM0012) no se actualizó el gramaje.")   

    prod13, created = Producto.objects.update_or_create(
        ID_PRODUCTO="AM0013",
        defaults={
        'PROD_CATEGORIA':cat1,
        'PROD_NOMBRE':"S-HTP",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':310.00,
        'PROD_PRECIO_PUB':370.00,
        'PROD_GRAMAJE':200.00
        }    
    )
    if created:
        print(f"Producto '{prod13.PROD_NOMBRE}' (AM0013) creado.")
    else:
        print(f"Producto '{prod13.PROD_NOMBRE}' (AM0013) ya existía. Actualizando gramaje.")
        prod13.PROD_GRAMAJE = 200.00
        prod13.save()
        print(f"Producto '{prod13.PROD_NOMBRE}' (AM0013) actualizado con gramaje.")


    prod14, created = Producto.objects.update_or_create(
        ID_PRODUCTO="AM0014",
        defaults={
        'PROD_CATEGORIA':cat1,
        'PROD_NOMBRE':"S-HTP",
        'CONTENIDO_PZS':"180 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':470.00,
        'PROD_PRECIO_PUB':560.00,
        'PROD_GRAMAJE':200.00
        }
        )
    if created:
        print(f"Producto '{prod14.PROD_NOMBRE}' (AM0014) creado.")
    else:
        print(f"Producto '{prod14.PROD_NOMBRE}' (AM0014) ya existía. Actualizando gramaje.")
        prod14.PROD_GRAMAJE = 200.00
        prod14.save()
        print(f"Producto '{prod14.PROD_NOMBRE}' (AM0014) actualizado con gramaje.")
    # NUTRACEUTICOS
    prod15, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU001",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"GABA",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':220.00,
        'PROD_PRECIO_PUB':280.00,
        }
    )
    if created:
        print(f"Producto '{prod15.PROD_NOMBRE}' (NU001) creado.")
    else:
        print(f"Producto '{prod15.PROD_NOMBRE}' (NU001) ya existía.")
        print(f"Producto '{prod15.PROD_NOMBRE}' (NU001) no se actualizó el gramaje.")

    prod16, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU002",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"CoQ10 COENZYME Q-10",
        'CONTENIDO_PZS':"30 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':182.00,
        'PROD_PRECIO_PUB':220.00,
        'PROD_GRAMAJE':100.00
        }
    )
    if created:
        print(f"Producto '{prod16.PROD_NOMBRE}' (NU002) creado.")
    else:
        print(f"Producto '{prod16.PROD_NOMBRE}' (NU002) ya existía. Actualizando gramaje.")
        prod16.PROD_GRAMAJE = 100.00
        prod16.save()
        print(f"Producto '{prod16.PROD_NOMBRE}' (NU002) actualizado con gramaje.")
    prod17, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU003",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"CoQ10 COENZYME Q-10",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':460.00,
        'PROD_PRECIO_PUB':550.00,
        'PROD_GRAMAJE':100.00
        }
    )
    if created:
        print(f"Producto '{prod17.PROD_NOMBRE}' (NU003) creado.")
    else:
        print(f"Producto '{prod17.PROD_NOMBRE}' (NU003) ya existía. Actualizando gramaje.")
        prod17.PROD_GRAMAJE = 100.00
        prod17.save()
        print(f"Producto '{prod17.PROD_NOMBRE}' (NU003) actualizado con gramaje.")
    
    prod18, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU004",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"CoQ10 COENZYME Q-10",
        'CONTENIDO_PZS':"30 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':410.00,
        'PROD_PRECIO_PUB':460.00,
        'PROD_GRAMAJE':400.00
        }
    )
    if created:
        print(f"Producto '{prod18.PROD_NOMBRE}' (NU004) creado.")
    else:
        print(f"Producto '{prod18.PROD_NOMBRE}' (NU004) ya existía. Actualizando gramaje.")
        prod18.PROD_GRAMAJE = 400.00
        prod18.save()
        print(f"Producto '{prod18.PROD_NOMBRE}' (NU004) actualizado con gramaje.")
    
    prod19, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU005",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"CoQ10 COENZYME Q-10",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':1020.00,
        'PROD_PRECIO_PUB':460.00,
        'PROD_GRAMAJE':400.00
        }
    )
    if created:
        print(f"Producto '{prod19.PROD_NOMBRE}' (NU005) creado.")
    else:
        print(f"Producto '{prod19.PROD_NOMBRE}' (NU005) ya existía. Actualizando gramaje.")
        prod19.PROD_GRAMAJE = 36.00
        prod19.save()
        print(f"Producto '{prod19.PROD_NOMBRE}' (NU005) actualizado con gramaje.")
    
    prod20, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU006",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"CURVE FEM",
        'CONTENIDO_PZS':"60 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':82.00,
        'PROD_PRECIO_PUB':130.00,
        }
    )
    if created:
        print(f"Producto '{prod20.PROD_NOMBRE}' (NU006) creado.")
    else:
        print(f"Producto '{prod20.PROD_NOMBRE}' (NU006) ya existía.")
        print(f"Producto '{prod20.PROD_NOMBRE}' (NU006) no se actualizó el gramaje.")

    prod21, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU007",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"MELATOTINA",
        'CONTENIDO_PZS':"60 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':164.00,
        'PROD_PRECIO_PUB':192.00,
        }
    )
    if created:
        print(f"Producto '{prod21.PROD_NOMBRE}' (NU007) creado.")
    else:
        print(f"Producto '{prod21.PROD_NOMBRE}' (NU007) ya existía.")
        print(f"Producto '{prod21.PROD_NOMBRE}' (NU007) no se actualizó el gramaje.")

    prod22, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU008",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"MELATOTINA",
        'CONTENIDO_PZS':"120 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':246.00,
        'PROD_PRECIO_PUB':296.00,
        }
        
    )
    if created:
        print(f"Producto '{prod22.PROD_NOMBRE}' (NU008) creado.")
    else:
        print(f"Producto '{prod22.PROD_NOMBRE}' (NU008) ya existía.")
        print(f"Producto '{prod22.PROD_NOMBRE}' (NU008) no se actualizó el gramaje.")
    
    prod23, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU009",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"KRILL HEALTH",
        'CONTENIDO_PZS':"60 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':130.00,
        'PROD_PRECIO_PUB':164.00,
        'PROD_GRAMAJE':512.50
        }
    )
    if created:
        print(f"Producto '{prod23.PROD_NOMBRE}' (NU009) creado.")
    else:
        print(f"Producto '{prod23.PROD_NOMBRE}' (NU009) ya existía. Actualizando gramaje.")
        prod23.PROD_GRAMAJE = 512.50
        prod23.save()
        print(f"Producto '{prod23.PROD_NOMBRE}' (NU009) actualizado con gramaje.")
    
    prod24, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU010",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"KRILL OIL",
        'CONTENIDO_PZS':"60 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':154.00,
        'PROD_PRECIO_PUB':192.00,
        'PROD_GRAMAJE':500.00
        }
    )
    if created:
        print(f"Producto '{prod24.PROD_NOMBRE}' (NU010) creado.")
    else:
        print(f"Producto '{prod24.PROD_NOMBRE}' (NU010) ya existía. Actualizando gramaje.")
        prod24.PROD_GRAMAJE = 500.00
        prod24.save()
        print(f"Producto '{prod24.PROD_NOMBRE}' (NU010) actualizado con gramaje.")

    prod25, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU011",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"OMEGA 3",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':164.00,
        'PROD_PRECIO_PUB':210.00,
        'PROD_GRAMAJE':1000.00
        }
    )
    if created:
        print(f"Producto '{prod25.PROD_NOMBRE}' (NU011) creado.")
    else:
        print(f"Producto '{prod25.PROD_NOMBRE}' (NU011) ya existía. Actualizando gramaje.")
        prod25.PROD_GRAMAJE = 1000.00
        prod25.save()
        print(f"Producto '{prod25.PROD_NOMBRE}' (NU011) actualizado con gramaje.")

    prod26, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU012",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"POLIFENOLES",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':520.00,
        'PROD_PRECIO_PUB':650.00,
        }
    )
    if created:
        print(f"Producto '{prod26.PROD_NOMBRE}' (NU012) creado.")
    else:
        print(f"Producto '{prod26.PROD_NOMBRE}' (NU012) ya existía.")
        print(f"Producto '{prod26.PROD_NOMBRE}' (NU012) no se actualizó el gramaje.")

    prod27, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU013",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"ACIDO ALFA LIPOICO",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':345.00,
        'PROD_PRECIO_PUB':420.00,
        'PROD_GRAMAJE':600.00
        }
    )
    if created:
        print(f"Producto '{prod27.PROD_NOMBRE}' (NU013) creado.")
    else:
        print(f"Producto '{prod27.PROD_NOMBRE}' (NU013) ya existía. Actualizando gramaje.")
        prod27.PROD_GRAMAJE = 600.00
        prod27.save()
        print(f"Producto '{prod27.PROD_NOMBRE}' (NU013) actualizado con gramaje.")

    prod28, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU014",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"ACIDO ALFA LIPOICO",
        'CONTENIDO_PZS':"180 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':645.00,
        'PROD_PRECIO_PUB':720.00,
        'PROD_GRAMAJE':600.00
        }
    )
    if created:
        print(f"Producto '{prod28.PROD_NOMBRE}' (NU014) creado.")
    else:
        print(f"Producto '{prod28.PROD_NOMBRE}' (NU014) ya existía. Actualizando gramaje.")
        prod28.PROD_GRAMAJE = 600.00
        prod28.save()
        print(f"Producto '{prod28.PROD_NOMBRE}' (NU014) actualizado con gramaje.")

    prod29, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU016",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"BERBERINE",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':370.00,
        'PROD_PRECIO_PUB':480.00,
        'PROD_GRAMAJE':1000.00
        }
    )
    if created:
        print(f"Producto '{prod29.PROD_NOMBRE}' (NU016) creado.")
    else:
        print(f"Producto '{prod29.PROD_NOMBRE}' (NU016) ya existía. Actualizando gramaje.")
        prod29.PROD_GRAMAJE = 1000.00
        prod29.save()
        print(f"Producto '{prod29.PROD_NOMBRE}' (NU016) actualizado con gramaje.")
    
    prod30, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU017",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"BERBERINE",
        'CONTENIDO_PZS':"160 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':550.00,
        'PROD_PRECIO_PUB':680.00,
        'PROD_GRAMAJE':1000.00
        }
    )
    if created:
        print(f"Producto '{prod30.PROD_NOMBRE}' (NU017) creado.")
    else:
        print(f"Producto '{prod30.PROD_NOMBRE}' (NU017) ya existía. Actualizando gramaje.")
        prod30.PROD_GRAMAJE = 1000.00
        prod30.save()
        print(f"Producto '{prod30.PROD_NOMBRE}' (NU017) actualizado con gramaje.")

    prod31, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU018",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"BERBERINE HEALTHY BALANCE",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':365.00,
        'PROD_PRECIO_PUB':470.00,
        'PROD_GRAMAJE':750.00
        }
    )
    if created:
        print(f"Producto '{prod31.PROD_NOMBRE}' (NU018) creado.")
    else:
        print(f"Producto '{prod31.PROD_NOMBRE}' (NU018) ya existía. Actualizando gramaje.")
        prod31.PROD_GRAMAJE = 750.00
        prod31.save()
        print(f"Producto '{prod31.PROD_NOMBRE}' (NU018) actualizado con gramaje.")

    prod32, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU019",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"BERBERINE HEALTHY BALANCE",
        'CONTENIDO_PZS':"160 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':520.00,
        'PROD_PRECIO_PUB':650.00,
        'PROD_GRAMAJE':750.00
        }
    )
    if created:
        print(f"Producto '{prod32.PROD_NOMBRE}' (NU019) creado.")
    else:
        print(f"Producto '{prod32.PROD_NOMBRE}' (NU019) ya existía. Actualizando gramaje.")
        prod32.PROD_GRAMAJE = 750.00
        prod32.save()
        print(f"Producto '{prod32.PROD_NOMBRE}' (NU019) actualizado con gramaje.")

    prod33, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU020",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"BIO GLUTATION LIPOSOMAL",
        'CONTENIDO_PZS':"30 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':202.00,
        'PROD_PRECIO_PUB':250.00,
        }
    )
    if created:
        print(f"Producto '{prod33.PROD_NOMBRE}' (NU020) creado.")
    else:
        print(f"Producto '{prod33.PROD_NOMBRE}' (NU020) ya existía.")
        print(f"Producto '{prod33.PROD_NOMBRE}' (NU020) no se actualizó el gramaje.")

    prod34, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU021",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"BIO GLUTATION LIPOSOMAL",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':520.00,
        'PROD_PRECIO_PUB':650.00,
        }
    )
    if created:
        print(f"Producto '{prod34.PROD_NOMBRE}' (NU021) creado.")
    else:
        print(f"Producto '{prod34.PROD_NOMBRE}' (NU021) ya existía.")
        print(f"Producto '{prod34.PROD_NOMBRE}' (NU021) no se actualizó el gramaje.")

    prod35, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU022",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"BIO GLUTATION LIPOSOMAL",
        'CONTENIDO_PZS':"160 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':840.00,
        'PROD_PRECIO_PUB':1050.00,
        }
    )
    if created:
        print(f"Producto '{prod35.PROD_NOMBRE}' (NU022) creado.")
    else:
        print(f"Producto '{prod35.PROD_NOMBRE}' (NU022) ya existía.")
        print(f"Producto '{prod35.PROD_NOMBRE}' (NU022) no se actualizó el gramaje.")

    prod36, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU023",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"BIO RESVERATROL",
        'CONTENIDO_PZS':"60 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':203.00,
        'PROD_PRECIO_PUB':254.00,
        }
    )
    if created:
        print(f"Producto '{prod36.PROD_NOMBRE}' (NU023) creado.")
    else:
        print(f"Producto '{prod36.PROD_NOMBRE}' (NU023) ya existía.")
        print(f"Producto '{prod36.PROD_NOMBRE}' (NU023) no se actualizó el gramaje.")

    prod37, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU024",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"BIO RESVERATROL",
        'CONTENIDO_PZS':"120 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':345.00,
        'PROD_PRECIO_PUB':430.00,
        }
    )
    if created:
        print(f"Producto '{prod37.PROD_NOMBRE}' (NU024) creado.")
    else:
        print(f"Producto '{prod37.PROD_NOMBRE}' (NU024) ya existía.")
        print(f"Producto '{prod37.PROD_NOMBRE}' (NU024) no se actualizó el gramaje.")

    prod38, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU025",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"BIO RESVERATROL",
        'CONTENIDO_PZS':"180 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':450.00,
        'PROD_PRECIO_PUB':550.00,
        }
    )
    if created:
        print(f"Producto '{prod38.PROD_NOMBRE}' (NU025) creado.")
    else:
        print(f"Producto '{prod38.PROD_NOMBRE}' (NU025) ya existía.")
        print(f"Producto '{prod38.PROD_NOMBRE}' (NU025) no se actualizó el gramaje.")

    prod39, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU026",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"COLAGENO 1000",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':196.00,
        'PROD_PRECIO_PUB':245.00,
        'PROD_GRAMAJE':1000.00
        }
    )
    if created:
        print(f"Producto '{prod39.PROD_NOMBRE}' (NU026) creado.")
    else:
        print(f"Producto '{prod39.PROD_NOMBRE}' (NU026) ya existía. Actualizando gramaje.")
        prod39.PROD_GRAMAJE = 1000.00
        prod39.save()
        print(f"Producto '{prod39.PROD_NOMBRE}' (NU026) actualizado con gramaje.")

    prod40, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU027",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"COLAGENO 1000",
        'CONTENIDO_PZS':"160 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':282.00,
        'PROD_PRECIO_PUB':354.00,
        'PROD_GRAMAJE':1000.00
        }
    )
    if created:
        print(f"Producto '{prod40.PROD_NOMBRE}' (NU027) creado.")
    else:
        print(f"Producto '{prod40.PROD_NOMBRE}' (NU027) ya existía. Actualizando gramaje.")
        prod40.PROD_GRAMAJE = 1000.00
        prod40.save()
        print(f"Producto '{prod40.PROD_NOMBRE}' (NU027) actualizado con gramaje.")

    prod41, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU028",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"COLAGENO NAD ADVANCE",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':380.00,
        'PROD_PRECIO_PUB':480.00,
        }
    )
    if created:
        print(f"Producto '{prod41.PROD_NOMBRE}' (NU028) creado.")
    else:
        print(f"Producto '{prod41.PROD_NOMBRE}' (NU028) ya existía.")
        print(f"Producto '{prod41.PROD_NOMBRE}' (NU028) no se actualizó el gramaje.")

    prod42, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU029",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"COLAGENO NAD ADVANCE",
        'CONTENIDO_PZS':"160 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':600.00,
        'PROD_PRECIO_PUB':750.00,
        }
    )
    if created:
        print(f"Producto '{prod42.PROD_NOMBRE}' (NU029) creado.")
    else:
        print(f"Producto '{prod42.PROD_NOMBRE}' (NU029) ya existía.")
        print(f"Producto '{prod42.PROD_NOMBRE}' (NU029) no se actualizó el gramaje.")

    prod43, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU030",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"GLUTABIOTIC GLUTATION & PROBIOTICOS",
        'CONTENIDO_PZS':"30 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':230.00,
        'PROD_PRECIO_PUB':290.00,
        }
    )
    prod44, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU031",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"GLUTABIOTIC GLUTATION & PROBIOTICOS",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':590.00,
        'PROD_PRECIO_PUB':740.00,
        }
    )
    if created:
        print(f"Producto '{prod44.PROD_NOMBRE}' (NU031) creado.")
    else:
        print(f"Producto '{prod44.PROD_NOMBRE}' (NU031) ya existía.")
        print(f"Producto '{prod44.PROD_NOMBRE}' (NU031) no se actualizó el gramaje.")

    prod45, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU032",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"GLUTABIOTIC GLUTATION & PROBIOTICOS",
        'CONTENIDO_PZS':"160 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':885.00,
        'PROD_PRECIO_PUB':1100.00,
        }
    )
    if created:
        print(f"Producto '{prod45.PROD_NOMBRE}' (NU032) creado.")
    else:
        print(f"Producto '{prod45.PROD_NOMBRE}' (NU032) ya existía.")
        print(f"Producto '{prod45.PROD_NOMBRE}' (NU032) no se actualizó el gramaje.")

    prod46, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU033",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"GLUTATION 600",
        'CONTENIDO_PZS':"30 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':202.00,
        'PROD_PRECIO_PUB':250.00,
        'PROD_GRAMAJE':600.00
        }
    )
    if created:
        print(f"Producto '{prod46.PROD_NOMBRE}' (NU033) creado.")
    else:
        print(f"Producto '{prod46.PROD_NOMBRE}' (NU033) ya existía. Actualizando gramaje.")
        prod46.PROD_GRAMAJE = 600.00
        prod46.save()
        print(f"Producto '{prod46.PROD_NOMBRE}' (NU033) actualizado con gramaje.")

    prod47 , created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU034",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"GLUTATION 600",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':520.00,
        'PROD_PRECIO_PUB':650.00,
        'PROD_GRAMAJE':600.00
        }
    )
    if created:
        print(f"Producto '{prod47.PROD_NOMBRE}' (NU034) creado.")
    else:
        print(f"Producto '{prod47.PROD_NOMBRE}' (NU034) ya existía. Actualizando gramaje.")
        prod47.PROD_GRAMAJE = 600.00
        prod47.save()
        print(f"Producto '{prod47.PROD_NOMBRE}' (NU034) actualizado con gramaje.")

    prod48, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU035",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"GLUTATION 600",
        'CONTENIDO_PZS':"160 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':840.00,
        'PROD_PRECIO_PUB':1050.00,
        'PROD_GRAMAJE':600.00
        }
    )
    if created:
        print(f"Producto '{prod48.PROD_NOMBRE}' (NU035) creado.")
    else:
        print(f"Producto '{prod48.PROD_NOMBRE}' (NU035) ya existía. Actualizando gramaje.")
        prod48.PROD_GRAMAJE = 600.00
        prod48.save()
        print(f"Producto '{prod48.PROD_NOMBRE}' (NU035) actualizado con gramaje.")

    prod49, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU036",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"GLUTATION ANTIOX PROTEC",
        'CONTENIDO_PZS':"30 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':230.00,
        'PROD_PRECIO_PUB':290.00,
        }
    )
    if created:
        print(f"Producto '{prod49.PROD_NOMBRE}' (NU036) creado.")
    else:
        print(f"Producto '{prod49.PROD_NOMBRE}' (NU036) ya existía.")
        print(f"Producto '{prod49.PROD_NOMBRE}' (NU036) no se actualizó el gramaje.")

    prod50, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU037",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"GLUTATION ANTIOX PROTEC",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':590.00,
        'PROD_PRECIO_PUB':740.00,
        }
    )
    if created:
        print(f"Producto '{prod50.PROD_NOMBRE}' (NU037) creado.")
    else:
        print(f"Producto '{prod50.PROD_NOMBRE}' (NU037) ya existía.")
        print(f"Producto '{prod50.PROD_NOMBRE}' (NU037) no se actualizó el gramaje.")

    prod51, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU038",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"GLUTATION ANTIOX PROTEC",
        'CONTENIDO_PZS':"160 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':885.00,
        'PROD_PRECIO_PUB':1100.00,
        }
    )
    if created:
        print(f"Producto '{prod51.PROD_NOMBRE}' (NU038) creado.")
    else:
        print(f"Producto '{prod51.PROD_NOMBRE}' (NU038) ya existía.")
        print(f"Producto '{prod51.PROD_NOMBRE}' (NU038) no se actualizó el gramaje.")

    prod52, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU039",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"NAD 600",
        'CONTENIDO_PZS':"30 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':280.00,
        'PROD_PRECIO_PUB':360.00,
        'PROD_GRAMAJE':600.00
        }
    )
    if created:
        print(f"Producto '{prod52.PROD_NOMBRE}' (NU039) creado.")
    else:
        print(f"Producto '{prod52.PROD_NOMBRE}' (NU039) ya existía. Actualizando gramaje.")
        prod52.PROD_GRAMAJE = 600.00
        prod52.save()
        print(f"Producto '{prod52.PROD_NOMBRE}' (NU039) actualizado con gramaje.")

    prod53, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU040",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"NAD 600",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':760.00,
        'PROD_PRECIO_PUB':950.00,
        'PROD_GRAMAJE':600.00
        }
    )
    if created:
        print(f"Producto '{prod53.PROD_NOMBRE}' (NU040) creado.")
    else:  
        print(f"Producto '{prod53.PROD_NOMBRE}' (NU040) ya existía. Actualizando gramaje.")
        prod53.PROD_GRAMAJE = 600.00
        prod53.save()
        print(f"Producto '{prod53.PROD_NOMBRE}' (NU040) actualizado con gramaje.")

    prod54, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU041",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"NAD 600",
        'CONTENIDO_PZS':"180 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':1300.00,
        'PROD_PRECIO_PUB':1650.00,
        'PROD_GRAMAJE':600.00
        }
    )
    if created:
        print(f"Producto '{prod54.PROD_NOMBRE}' (NU041) creado.")
    else:
        print(f"Producto '{prod54.PROD_NOMBRE}' (NU041) ya existía. Actualizando gramaje.")
        prod54.PROD_GRAMAJE = 600.00
        prod54.save()
        print(f"Producto '{prod54.PROD_NOMBRE}' (NU041) actualizado con gramaje.")

    prod55, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU042",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"NAD ADVANCE LIPOSOMAL",
        'CONTENIDO_PZS':"30 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':304.00,
        'PROD_PRECIO_PUB':380.00,
        }
    )
    if created:
        print(f"Producto '{prod55.PROD_NOMBRE}' (NU042) creado.")
    else:
        print(f"Producto '{prod55.PROD_NOMBRE}' (NU042) ya existía.")
        print(f"Producto '{prod55.PROD_NOMBRE}' (NU042) no se actualizó el gramaje.")

    prod56, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU043",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"NAD ADVANCE LIPOSOMAL",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':840.00,
        'PROD_PRECIO_PUB':1050.00,
        }
    )
    if created:
        print(f"Producto '{prod56.PROD_NOMBRE}' (NU043) creado.")
    else:
        print(f"Producto '{prod56.PROD_NOMBRE}' (NU043) ya existía.")
        print(f"Producto '{prod56.PROD_NOMBRE}' (NU043) no se actualizó el gramaje.")

    prod57, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU044",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"NAD ADVANCE LIPOSOMAL",
        'CONTENIDO_PZS':"160 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':1400.00,
        'PROD_PRECIO_PUB':1750.00,
        }
    )
    if created:
        print(f"Producto '{prod57.PROD_NOMBRE}' (NU044) creado.")
    else:
        print(f"Producto '{prod57.PROD_NOMBRE}' (NU044) ya existía.")
        print(f"Producto '{prod57.PROD_NOMBRE}' (NU044) no se actualizó el gramaje.")

    prod58, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU045",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"RESVERATROL ADVANCE FORTE",
        'CONTENIDO_PZS':"30 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':130.00,
        'PROD_PRECIO_PUB':165.00,
        }
    )
    if created:
        print(f"Producto '{prod58.PROD_NOMBRE}' (NU045) creado.")
    else:
        print(f"Producto '{prod58.PROD_NOMBRE}' (NU045) ya existía.")
        print(f"Producto '{prod58.PROD_NOMBRE}' (NU045) no se actualizó el gramaje.")

    prod59, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU046",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"RESVERATROL ADVANCE FORTE",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':310.00,
        'PROD_PRECIO_PUB':380.00,
        }
    )
    if created:
        print(f"Producto '{prod59.PROD_NOMBRE}' (NU046) creado.")
    else:
        print(f"Producto '{prod59.PROD_NOMBRE}' (NU046) ya existía.")
        print(f"Producto '{prod59.PROD_NOMBRE}' (NU046) no se actualizó el gramaje.")

    prod60, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU047",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"RESVERATROL ADVANCE FORTE",
        'CONTENIDO_PZS':"160 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':460.00,
        'PROD_PRECIO_PUB':575.00,
        }
    )
    if created:
        print(f"Producto '{prod60.PROD_NOMBRE}' (NU047) creado.")
    else:
        print(f"Producto '{prod60.PROD_NOMBRE}' (NU047) ya existía.")
        print(f"Producto '{prod60.PROD_NOMBRE}' (NU047) no se actualizó el gramaje.")

    prod61, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU048",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"TRANS RESVERATROL NAD ADVANCE LIPOSOMAL",
        'CONTENIDO_PZS':"30 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':230.00,
        'PROD_PRECIO_PUB':290.00,
        }
    )
    if created:
        print(f"Producto '{prod61.PROD_NOMBRE}' (NU048) creado.")
    else:
        print(f"Producto '{prod61.PROD_NOMBRE}' (NU048) ya existía.")
        print(f"Producto '{prod61.PROD_NOMBRE}' (NU048) no se actualizó el gramaje.")

    prod62, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU049",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"TRANS RESVERATROL NAD ADVANCE LIPOSOMAL",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':600.00,
        'PROD_PRECIO_PUB':750.00,
        }
    )
    if created:
        print(f"Producto '{prod62.PROD_NOMBRE}' (NU049) creado.")
    else:
        print(f"Producto '{prod62.PROD_NOMBRE}' (NU049) ya existía.")
        print(f"Producto '{prod62.PROD_NOMBRE}' (NU049) no se actualizó el gramaje.")
        
    prod63, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU050",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"TRANS RESVERATROL NAD ADVANCE LIPOSOMAL",
        'CONTENIDO_PZS':"160 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':960.00,
        'PROD_PRECIO_PUB':1200.00,
        }
    )
    if created:
        print(f"Producto '{prod63.PROD_NOMBRE}' (NU050) creado.")
    else:
        print(f"Producto '{prod63.PROD_NOMBRE}' (NU050) ya existía.")
        print(f"Producto '{prod63.PROD_NOMBRE}' (NU050) no se actualizó el gramaje.")

    prod64, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU051",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"RESVERATROL & NAD RADIANCE ADVANCE",
        'CONTENIDO_PZS':"30 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':304.00,
        'PROD_PRECIO_PUB':380.00,
        }
    )
    if created:
        print(f"Producto '{prod64.PROD_NOMBRE}' (NU051) creado.")
    else:
        print(f"Producto '{prod64.PROD_NOMBRE}' (NU051) ya existía.")
        print(f"Producto '{prod64.PROD_NOMBRE}' (NU051) no se actualizó el gramaje.")

    prod65, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU052",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"RESVERATROL & NAD RADIANCE ADVANCE",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':740.00,
        'PROD_PRECIO_PUB':920.00,
        }
    )
    if created:
        print(f"Producto '{prod65.PROD_NOMBRE}' (NU052) creado.")
    else:
        print(f"Producto '{prod65.PROD_NOMBRE}' (NU052) ya existía.")
        print(f"Producto '{prod65.PROD_NOMBRE}' (NU052) no se actualizó el gramaje.")

    prod66, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU053",
        defaults={
        'PROD_CATEGORIA':cat2,
        'PROD_NOMBRE':"RESVERATROL & NAD RADIANCE ADVANCE",
        'CONTENIDO_PZS':"160 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':1100.00,
        'PROD_PRECIO_PUB':1400.00,
        }
    )
    if created:
        print(f"Producto '{prod66.PROD_NOMBRE}' (NU053) creado.")
    else:
        print(f"Producto '{prod66.PROD_NOMBRE}' (NU053) ya existía.")
        print(f"Producto '{prod66.PROD_NOMBRE}' (NU053) no se actualizó el gramaje.")
    # ANTIOXIDANTES
    prod67, created = Producto.objects.update_or_create(
        ID_PRODUCTO="AN001",
        defaults={
        'PROD_CATEGORIA':cat3,
        'PROD_NOMBRE':"ASTAXANTINA",
        'CONTENIDO_PZS':"30 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':224.00,
        'PROD_PRECIO_PUB':280.00,
        'PROD_GRAMAJE':20.00
        }
    )
    if created:
        print(f"Producto '{prod67.PROD_NOMBRE}' (AN001) creado.")
    else:
        print(f"Producto '{prod67.PROD_NOMBRE}' (AN001) ya existía. Actualizando gramaje.")
        prod67.PROD_GRAMAJE = .60
        prod67.save()
        print(f"Producto '{prod67.PROD_NOMBRE}' (AN001) actualizado con gramaje.")

    prod68, created = Producto.objects.update_or_create(
        ID_PRODUCTO="AN002",
        defaults={
        'PROD_CATEGORIA':cat3,
        'PROD_NOMBRE':"ASTAXANTINA",
        'CONTENIDO_PZS':"60 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':590.00,
        'PROD_PRECIO_PUB':740.00,
        'PROD_GRAMAJE':20.00
        }
    )
    if created:
        print(f"Producto '{prod68.PROD_NOMBRE}' (AN002) creado.")
    else:
        print(f"Producto '{prod68.PROD_NOMBRE}' (AN002) ya existía. Actualizando gramaje.")
        prod68.PROD_GRAMAJE = 20.00
        prod68.save()
        print(f"Producto '{prod68.PROD_NOMBRE}' (AN002) actualizado con gramaje.")

    prod69, created = Producto.objects.update_or_create(
        ID_PRODUCTO="AN003",
        defaults={
        'PROD_CATEGORIA':cat3,
        'PROD_NOMBRE':"QUERCETINA",
        'CONTENIDO_PZS':"60 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':290.00,
        'PROD_PRECIO_PUB':354.00,
        'PROD_GRAMAJE':500.00
        }
    )
    if created:
        print(f"Producto '{prod69.PROD_NOMBRE}' (AN003) creado.")
    else:
        print(f"Producto '{prod69.PROD_NOMBRE}' (AN003) ya existía. Actualizando gramaje.")
        prod69.PROD_GRAMAJE = 500.00
        prod69.save()
        print(f"Producto '{prod69.PROD_NOMBRE}' (AN003) actualizado con gramaje.")

    prod70, created = Producto.objects.update_or_create(
        ID_PRODUCTO="AN004",
        defaults={
        'PROD_CATEGORIA':cat3,
        'PROD_NOMBRE':"QUERCETINA",
        'CONTENIDO_PZS':"120 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':480.00,
        'PROD_PRECIO_PUB':600.00,
        'PROD_GRAMAJE':500.00
        }
    )
    if created:
        print(f"Producto '{prod70.PROD_NOMBRE}' (AN004) creado.")
    else:
        print(f"Producto '{prod70.PROD_NOMBRE}' (AN004) ya existía. Actualizando gramaje.")
        prod70.PROD_GRAMAJE = 500.00
        prod70.save()
        print(f"Producto '{prod70.PROD_NOMBRE}' (AN004) actualizado con gramaje.")

    prod71, created = Producto.objects.update_or_create(
        ID_PRODUCTO="AN005",
        defaults={
        'PROD_CATEGORIA':cat3,
        'PROD_NOMBRE':"AXTRIOM (ASTAXANTINA FORTE)",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':590.00,
        'PROD_PRECIO_PUB':740.00,
        }
    )
    if created:
        print(f"Producto '{prod71.PROD_NOMBRE}' (AN005) creado.")
    else:
        print(f"Producto '{prod71.PROD_NOMBRE}' (AN005) ya existía.")
        print(f"Producto '{prod71.PROD_NOMBRE}' (AN005) no se actualizó el gramaje.")

    prod72, created = Producto.objects.update_or_create(
        ID_PRODUCTO="AN006",
        defaults={
        'PROD_CATEGORIA':cat3,
        'PROD_NOMBRE':"QUERTIOM (QUERCETINA FORTE)",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':590.00,
        'PROD_PRECIO_PUB':740.00,
        }
    )
    if created:
        print(f"Producto '{prod72.PROD_NOMBRE}' (AN006) creado.")
    else :
        print(f"Producto '{prod72.PROD_NOMBRE}' (AN006) ya existía.")
        print(f"Producto '{prod72.PROD_NOMBRE}' (AN006) no se actualizó el gramaje.")


    # VITAMINAS
    prod73, created = Producto.objects.update_or_create(
        ID_PRODUCTO="VI001",
        defaults={
        'PROD_CATEGORIA':cat4,
        'PROD_NOMBRE':"BIOTINA COMPLEX 10,00 MCG",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':230.00,
        'PROD_PRECIO_PUB':288.00,
        'PROD_GRAMAJE':.0009
        }
    )
    if created:
        print(f"Producto '{prod73.PROD_NOMBRE}' (VI001) creado.")
    else:
        print(f"Producto '{prod73.PROD_NOMBRE}' (VI001) ya existía. Actualizando gramaje.")
        prod73.PROD_GRAMAJE = .0009
        prod73.save()
        print(f"Producto '{prod73.PROD_NOMBRE}' (VI001) actualizado con gramaje.")

    prod74, created = Producto.objects.update_or_create(
        ID_PRODUCTO="VI002",
        defaults={
        'PROD_CATEGORIA':cat4,
        'PROD_NOMBRE':"COMPLEJO B",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':192.00,
        'PROD_PRECIO_PUB':230.00,
        }
    )
    if created:
        print(f"Producto '{prod74.PROD_NOMBRE}' (VI002) creado.")
    else:
        print(f"Producto '{prod74.PROD_NOMBRE}' (VI002) ya existía.")
        print(f"Producto '{prod74.PROD_NOMBRE}' (VI002) no se actualizó el gramaje.")

    prod75, created = Producto.objects.update_or_create(
        ID_PRODUCTO="VI003",
        defaults={
        'PROD_CATEGORIA':cat4,
        'PROD_NOMBRE':"COMPLEJO B",
        'CONTENIDO_PZS':"180 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':320.00,
        'PROD_PRECIO_PUB':380.00,
        }
    )
    if created:
        print(f"Producto '{prod75.PROD_NOMBRE}' (VI003) creado.")
    else:
        print(f"Producto '{prod75.PROD_NOMBRE}' (VI003) ya existía.")
        print(f"Producto '{prod75.PROD_NOMBRE}' (VI003) no se actualizó el gramaje.")

    prod76, created = Producto.objects.update_or_create(
        ID_PRODUCTO="VI004",
        defaults={
        'PROD_CATEGORIA':cat4,
        'PROD_NOMBRE':"VITAMINA C 500",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':182.00,
        'PROD_PRECIO_PUB':230.00,
        'PROD_GRAMAJE':500.00
        }
    )
    if created:
        print(f"Producto '{prod76.PROD_NOMBRE}' (VI004) creado.")
    else:
        print(f"Producto '{prod76.PROD_NOMBRE}' (VI004) ya existía. Actualizando gramaje.")
        prod76.PROD_GRAMAJE = 500.00
        prod76.save()
        print(f"Producto '{prod76.PROD_NOMBRE}' (VI004) actualizado con gramaje.")

    prod77, created = Producto.objects.update_or_create(
        ID_PRODUCTO="VI005",
        defaults={
        'PROD_CATEGORIA':cat4,
        'PROD_NOMBRE':"VITAMINA C 500",
        'CONTENIDO_PZS':"180 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':304.00,
        'PROD_PRECIO_PUB':380.00,
        'PROD_GRAMAJE':500.00
        }
    )
    if created:
        print(f"Producto '{prod77.PROD_NOMBRE}' (VI005) creado.")
    else:
        print(f"Producto '{prod77.PROD_NOMBRE}' (VI005) ya existía. Actualizando gramaje.")
        prod77.PROD_GRAMAJE = 500.00
        prod77.save()
        print(f"Producto '{prod77.PROD_NOMBRE}' (VI005) actualizado con gramaje.")

    prod78, created = Producto.objects.update_or_create(
        ID_PRODUCTO="VI006",
        defaults={
        'PROD_CATEGORIA':cat4,
        'PROD_NOMBRE':"VITAMINA C 1000",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':224.00,
        'PROD_PRECIO_PUB':280.00,
        'PROD_GRAMAJE':1000.00
        }
    )
    if created:
        print(f"Producto '{prod78.PROD_NOMBRE}' (VI006) creado.")
    else:
        print(f"Producto '{prod78.PROD_NOMBRE}' (VI006) ya existía. Actualizando gramaje.")
        prod78.PROD_GRAMAJE = 1000.00
        prod78.save()
        print(f"Producto '{prod78.PROD_NOMBRE}' (VI006) actualizado con gramaje.")

    prod79, created = Producto.objects.update_or_create(
        ID_PRODUCTO="VI007",
        defaults={
        'PROD_CATEGORIA':cat4,
        'PROD_NOMBRE':"VITAMINA C 1000",
        'CONTENIDO_PZS':"160 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':364.00,
        'PROD_PRECIO_PUB':460.00,
        'PROD_GRAMAJE':1000.00
        }
    )
    if created:
        print(f"Producto '{prod79.PROD_NOMBRE}' (VI007) creado.")
    else:
        print(f"Producto '{prod79.PROD_NOMBRE}' (VI007) ya existía. Actualizando gramaje.")
        prod79.PROD_GRAMAJE = 1000.00
        prod79.save()
        print(f"Producto '{prod79.PROD_NOMBRE}' (VI007) actualizado con gramaje.")

    prod80, created = Producto.objects.update_or_create(
        ID_PRODUCTO="VI008",
        defaults={
        'PROD_CATEGORIA':cat4,
        'PROD_NOMBRE':"VITAMINA D3 5000 UI",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':210.00,
        'PROD_PRECIO_PUB':265.00,
        'PROD_GRAMAJE':5000.00
        }
    )
    if created:
        print(f"Producto '{prod80.PROD_NOMBRE}' (VI008) creado.")
    else:
        print(f"Producto '{prod80.PROD_NOMBRE}' (VI008) ya existía. Actualizando gramaje.")
        prod80.PROD_GRAMAJE = 5000.00
        prod80.save()
        print(f"Producto '{prod80.PROD_NOMBRE}' (VI008) actualizado con gramaje.")

    prod81, created = Producto.objects.update_or_create(
        ID_PRODUCTO="VI009",
        defaults={
        'PROD_CATEGORIA':cat4,
        'PROD_NOMBRE':"VITAMINA D3 5000 UI",
        'CONTENIDO_PZS':"160 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':336.00,
        'PROD_PRECIO_PUB':420.00,
        'PROD_GRAMAJE':5000.00
        }
    )
    if created:
        print(f"Producto '{prod81.PROD_NOMBRE}' (VI009) creado.")
    else:
        print(f"Producto '{prod81.PROD_NOMBRE}' (VI009) ya existía. Actualizando gramaje.")
        prod81.PROD_GRAMAJE = 5000.00
        prod81.save()
        print(f"Producto '{prod81.PROD_NOMBRE}' (VI009) actualizado con gramaje.")

    prod82, created = Producto.objects.update_or_create(
        ID_PRODUCTO="VI010",
        defaults={
        'PROD_CATEGORIA':cat4,
        'PROD_NOMBRE':"VITAMINA E 400 UI",
        'CONTENIDO_PZS':"60 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':102.00,
        'PROD_PRECIO_PUB':120.00,
        'PROD_GRAMAJE':400.00
        }
    )
    if created:
        print(f"Producto '{prod82.PROD_NOMBRE}' (VI010) creado.")
    else:
        print(f"Producto '{prod82.PROD_NOMBRE}' (VI010) ya existía. Actualizando gramaje.")
        prod82.PROD_GRAMAJE = 400.00
        prod82.save()
        print(f"Producto '{prod82.PROD_NOMBRE}' (VI010) actualizado con gramaje.")

    prod83, created = Producto.objects.update_or_create(
        ID_PRODUCTO="VI011",
        defaults={
        'PROD_CATEGORIA':cat4,
        'PROD_NOMBRE':"VITAMINA E 400 UI",
        'CONTENIDO_PZS':"120 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':182.00,
        'PROD_PRECIO_PUB':220.00,
        'PROD_GRAMAJE':400.00
        }
    )
    if created:
        print(f"Producto '{prod83.PROD_NOMBRE}' (VI011) creado.")
    else:
        print(f"Producto '{prod83.PROD_NOMBRE}' (VI011) ya existía. Actualizando gramaje.")
        prod83.PROD_GRAMAJE = 400.00
        prod83.save()
        print(f"Producto '{prod83.PROD_NOMBRE}' (VI011) actualizado con gramaje.")

    prod84, created = Producto.objects.update_or_create(
        ID_PRODUCTO="VI012",
        defaults={
        'PROD_CATEGORIA':cat4,
        'PROD_NOMBRE':"VITAMINA E 1000 UI",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':254.00,
        'PROD_PRECIO_PUB':320.00,
        'PROD_GRAMAJE':1000.00
        }
    )
    if created:
        print(f"Producto '{prod84.PROD_NOMBRE}' (VI012) creado.")
    else:
        print(f"Producto '{prod84.PROD_NOMBRE}' (VI012) ya existía. Actualizando gramaje.")
        prod84.PROD_GRAMAJE = 1000.00
        prod84.save()
        print(f"Producto '{prod84.PROD_NOMBRE}' (VI012) actualizado con gramaje.")

    prod85, created = Producto.objects.update_or_create(
        ID_PRODUCTO="VI013",
        defaults={
        'PROD_CATEGORIA':cat4,
        'PROD_NOMBRE':"VITAMINA D3 5000 UI",
        'CONTENIDO_PZS':"30 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':83.00,
        'PROD_PRECIO_PUB':110.00,
        'PROD_GRAMAJE':5000.00
        }
    )
    if created:
        print(f"Producto '{prod85.PROD_NOMBRE}' (VI013) creado.")
    else:
        print(f"Producto '{prod85.PROD_NOMBRE}' (VI013) ya existía. Actualizando gramaje.")
        prod85.PROD_GRAMAJE = 5000.00
        prod85.save()
        print(f"Producto '{prod85.PROD_NOMBRE}' (VI013) actualizado con gramaje.")

    prod86, created = Producto.objects.update_or_create(
        ID_PRODUCTO="VI0130",
        defaults={
        'PROD_CATEGORIA':cat4,
        'PROD_NOMBRE':"VITAMINA D3 & K2",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':224.00,
        'PROD_PRECIO_PUB':280.00,
        }
    )
    if created:
        print(f"Producto '{prod86.PROD_NOMBRE}' (VI0130) creado.")
    else:
        print(f"Producto '{prod86.PROD_NOMBRE}' (VI0130) ya existía.")
        print(f"Producto '{prod86.PROD_NOMBRE}' (VI0130) no se actualizó el gramaje.")

    prod87, created = Producto.objects.update_or_create(
        ID_PRODUCTO="VI014",
        defaults={
        'PROD_CATEGORIA':cat4,
        'PROD_NOMBRE':"VITAMINA E 1000 UI",
        'CONTENIDO_PZS':"30 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':92.00,
        'PROD_PRECIO_PUB':120.00,
        'PROD_GRAMAJE':1000.00
        }
    )
    if created:
        print(f"Producto '{prod87.PROD_NOMBRE}' (VI014) creado.")
    else:
        print(f"Producto '{prod87.PROD_NOMBRE}' (VI014) ya existía. Actualizando gramaje.")
        prod87.PROD_GRAMAJE = 1000.00
        prod87.save()
        print(f"Producto '{prod87.PROD_NOMBRE}' (VI014) actualizado con gramaje.")
        

    # MINERALES
    prod88, created = Producto.objects.update_or_create(
        ID_PRODUCTO="MI001",
        defaults={
        'PROD_CATEGORIA':cat5,
        'PROD_NOMBRE':"CALCIO CON VITAMINA D3",
        'CONTENIDO_PZS':"60 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':224.00,
        'PROD_PRECIO_PUB':280.00,
        }
    )
    if created:
        print(f"Producto '{prod88.PROD_NOMBRE}' (MI001) creado.")
    else:
        print(f"Producto '{prod88.PROD_NOMBRE}' (MI001) ya existía.")
        print(f"Producto '{prod88.PROD_NOMBRE}' (MI001) no se actualizó el gramaje.")

    prod89, created = Producto.objects.update_or_create(
        ID_PRODUCTO="MI002",
        defaults={
        'PROD_CATEGORIA':cat5,
        'PROD_NOMBRE':"CALCIO CON VITAMINA D3",
        'CONTENIDO_PZS':"160 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':336.00,
        'PROD_PRECIO_PUB':420.00,
        }
    )
    if created:
        print(f"Producto '{prod89.PROD_NOMBRE}' (MI002) creado.")
    else:
        print(f"Producto '{prod89.PROD_NOMBRE}' (MI002) ya existía.")
        print(f"Producto '{prod89.PROD_NOMBRE}' (MI002) no se actualizó el gramaje.")

    prod90, created = Producto.objects.update_or_create(
        ID_PRODUCTO="MI003",
        defaults={
        'PROD_CATEGORIA':cat5,
        'PROD_NOMBRE':"COBRE (gluconato)",
        'CONTENIDO_PZS':"60 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':136.00,
        'PROD_PRECIO_PUB':174.00,
        }
    )
    if created:
        print(f"Producto '{prod90.PROD_NOMBRE}' (MI003) creado.")
    else:
        print(f"Producto '{prod90.PROD_NOMBRE}' (MI003) ya existía.")
        print(f"Producto '{prod90.PROD_NOMBRE}' (MI003) no se actualizó el gramaje.")

    prod91, created = Producto.objects.update_or_create(
        ID_PRODUCTO="MI004",
        defaults={
        'PROD_CATEGORIA':cat5,
        'PROD_NOMBRE':"COBRE (gluconato)",
        'CONTENIDO_PZS':"120 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':224.00,
        'PROD_PRECIO_PUB':280.00,
        }
    )
    if created:
        print(f"Producto '{prod91.PROD_NOMBRE}' (MI004) creado.")
    else:
        print(f"Producto '{prod91.PROD_NOMBRE}' (MI004) ya existía.")
        print(f"Producto '{prod91.PROD_NOMBRE}' (MI004) no se actualizó el gramaje.")

    prod92, created = Producto.objects.update_or_create(
        ID_PRODUCTO="MI005",
        defaults={
        'PROD_CATEGORIA':cat5,
        'PROD_NOMBRE':"MAGNESIO (Citrato)",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':182.00,
        'PROD_PRECIO_PUB':230.00,
        }
    )
    if created:
        print(f"Producto '{prod92.PROD_NOMBRE}' (MI005) creado.")
    else:
        print(f"Producto '{prod92.PROD_NOMBRE}' (MI005) ya existía.")
        print(f"Producto '{prod92.PROD_NOMBRE}' (MI005) no se actualizó el gramaje.")

    prod93, created = Producto.objects.update_or_create(
        ID_PRODUCTO="MI006",
        defaults={
        'PROD_CATEGORIA':cat5,
        'PROD_NOMBRE':"MAGNESIO (Citrato)",
        'CONTENIDO_PZS':"160 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':304.00,
        'PROD_PRECIO_PUB':380.00,
        }
    )
    if created:
        print(f"Producto '{prod93.PROD_NOMBRE}' (MI006) creado.")
    else:
        print(f"Producto '{prod93.PROD_NOMBRE}' (MI006) ya existía.")
        print(f"Producto '{prod93.PROD_NOMBRE}' (MI006) no se actualizó el gramaje.")

    prod94, created = Producto.objects.update_or_create(
        ID_PRODUCTO="MI007",
        defaults={
        'PROD_CATEGORIA':cat5,
        'PROD_NOMBRE':"POTASIO (Citrato)",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':145.00,
        'PROD_PRECIO_PUB':182.00,
        }
    )
    if created:
        print(f"Producto '{prod94.PROD_NOMBRE}' (MI007) creado.")
    else:
        print(f"Producto '{prod94.PROD_NOMBRE}' (MI007) ya existía.")
        print(f"Producto '{prod94.PROD_NOMBRE}' (MI007) no se actualizó el gramaje.")

    prod95, created = Producto.objects.update_or_create(
        ID_PRODUCTO="MI008",
        defaults={
        'PROD_CATEGORIA':cat5,
        'PROD_NOMBRE':"POTASIO (Citrato)",
        'CONTENIDO_PZS':"180 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':256.00,
        'PROD_PRECIO_PUB':320.00,
        }
    )
    if created:
        print(f"Producto '{prod95.PROD_NOMBRE}' (MI008) creado.")
    else:
        print(f"Producto '{prod95.PROD_NOMBRE}' (MI008) ya existía.")
        print(f"Producto '{prod95.PROD_NOMBRE}' (MI008) no se actualizó el gramaje.")

    prod96, created = Producto.objects.update_or_create(
        ID_PRODUCTO="MI009",
        defaults={
        'PROD_CATEGORIA':cat5,
        'PROD_NOMBRE':"SELENIO 220 ug (Selenito de sodio",
        'CONTENIDO_PZS':"60 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':146.00,
        'PROD_PRECIO_PUB':182.00,
        'PROD_GRAMAJE':220.00
        }
    )
    if created:
        print(f"Producto '{prod96.PROD_NOMBRE}' (MI009) creado.")
    else:
        print(f"Producto '{prod96.PROD_NOMBRE}' (MI009) ya existía. Actualizando gramaje.")
        prod96.PROD_GRAMAJE = 220.00
        prod96.save()
        print(f"Producto '{prod96.PROD_NOMBRE}' (MI009) actualizado con gramaje.")

    prod97, created = Producto.objects.update_or_create(
        ID_PRODUCTO="MI010",
        defaults={
        'PROD_CATEGORIA':cat5,
        'PROD_NOMBRE':"SELENIO 220 ug (Selenito de sodio)",
        'CONTENIDO_PZS':"120 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':230.00,
        'PROD_PRECIO_PUB':290.00,
        'PROD_GRAMAJE':220.00
        }
    )
    if created:
        print(f"Producto '{prod97.PROD_NOMBRE}' (MI010) creado.")
    else:
        print(f"Producto '{prod97.PROD_NOMBRE}' (MI010) ya existía. Actualizando gramaje.")
        prod97.PROD_GRAMAJE = 220.00
        prod97.save()
        print(f"Producto '{prod97.PROD_NOMBRE}' (MI010) actualizado con gramaje.")

    prod98, created = Producto.objects.update_or_create(
        ID_PRODUCTO="MI011",
        defaults={
        'PROD_CATEGORIA':cat5,
        'PROD_NOMBRE':"ZINC 50 (Citrato)",
        'CONTENIDO_PZS':"60 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':92.00,
        'PROD_PRECIO_PUB':120.00,
        'PROD_GRAMAJE':50.00
        }
    )
    if created:
        print(f"Producto '{prod98.PROD_NOMBRE}' (MI011) creado.")
    else:
        print(f"Producto '{prod98.PROD_NOMBRE}' (MI011) ya existía. Actualizando gramaje.")
        prod98.PROD_GRAMAJE = 50.00
        prod98.save()
        print(f"Producto '{prod98.PROD_NOMBRE}' (MI011) actualizado con gramaje.")

    prod99, created = Producto.objects.update_or_create(
        ID_PRODUCTO="MI012",
        defaults={
        'PROD_CATEGORIA':cat5,
        'PROD_NOMBRE':"ZINC 50 (Citrato)",
        'CONTENIDO_PZS':"120 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':210.00,
        'PROD_PRECIO_PUB':265.00,
        'PROD_GRAMAJE':50.00
        }
    )
    if created:
        print(f"Producto '{prod99.PROD_NOMBRE}' (MI012) creado.")
    else:
        print(f"Producto '{prod99.PROD_NOMBRE}' (MI012) ya existía. Actualizando gramaje.")
        prod99.PROD_GRAMAJE = 50.00
        prod99.save()
        print(f"Producto '{prod99.PROD_NOMBRE}' (MI012) actualizado con gramaje.")


    prod100, created = Producto.objects.update_or_create(
        ID_PRODUCTO="MI013",
        defaults={
        'PROD_CATEGORIA':cat5,
        'PROD_NOMBRE':"HIERRO (gluconato)",
        'CONTENIDO_PZS':"60 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':92.00,
        'PROD_PRECIO_PUB':120.00,
        }
    )
    if created:
        print(f"Producto '{prod100.PROD_NOMBRE}' (MI013) creado.")
    else:
        print(f"Producto '{prod100.PROD_NOMBRE}' (MI013) ya existía.")
        print(f"Producto '{prod100.PROD_NOMBRE}' (MI013) no se actualizó el gramaje.")

    prod101, created = Producto.objects.update_or_create(
        ID_PRODUCTO="MI014",
        defaults={
        'PROD_CATEGORIA':cat5,
        'PROD_NOMBRE':"HIERRO (gluconato)",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':122.00,
        'PROD_PRECIO_PUB':154.00,
        }
    )
    if created:
        print(f"Producto '{prod101.PROD_NOMBRE}' (MI014) creado.")
    else:
        print(f"Producto '{prod101.PROD_NOMBRE}' (MI014) ya existía.")
        print(f"Producto '{prod101.PROD_NOMBRE}' (MI014) no se actualizó el gramaje.")

    prod102, created = Producto.objects.update_or_create(
        ID_PRODUCTO="MI015",
        defaults={
        'PROD_CATEGORIA':cat5,
        'PROD_NOMBRE':"GLICINATO DE MAGNESIO",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':220.00,
        'PROD_PRECIO_PUB':174.00,
        }
    )
    if created:
        print(f"Producto '{prod102.PROD_NOMBRE}' (MI015) creado.")
    else:
        print(f"Producto '{prod102.PROD_NOMBRE}' (MI015) ya existía.")
        print(f"Producto '{prod102.PROD_NOMBRE}' (MI015) no se actualizó el gramaje.")

    prod103, created = Producto.objects.update_or_create(
        ID_PRODUCTO="MI016",
        defaults={
        'PROD_CATEGORIA':cat5,
        'PROD_NOMBRE':"TRIPLE MAGNESIO",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':174.00,
        'PROD_PRECIO_PUB':220.00,
        }
    )
    if created:
        print(f"Producto '{prod103.PROD_NOMBRE}' (MI016) creado.")
    else:
        print(f"Producto '{prod103.PROD_NOMBRE}' (MI016) ya existía.")
        print(f"Producto '{prod103.PROD_NOMBRE}' (MI016) no se actualizó el gramaje.")

    prod104, created = Producto.objects.update_or_create(
        ID_PRODUCTO="MI017",
        defaults={
        'PROD_CATEGORIA':cat5,
        'PROD_NOMBRE':"MAGNESIO / POTASIO",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':203.00,
        'PROD_PRECIO_PUB':264.00,
        }
    )
    if created:
        print(f"Producto '{prod104.PROD_NOMBRE}' (MI017) creado.")
    else:
        print(f"Producto '{prod104.PROD_NOMBRE}' (MI017) ya existía.")
        print(f"Producto '{prod104.PROD_NOMBRE}' (MI017) no se actualizó el gramaje.")

    prod105, created = Producto.objects.update_or_create(
        ID_PRODUCTO="MI018",
        defaults={
        'PROD_CATEGORIA':cat5,
        'PROD_NOMBRE':"MAGNESIO / ZINC",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':192.00,
        'PROD_PRECIO_PUB':245.00,
        }
    )
    if created:
        print(f"Producto '{prod105.PROD_NOMBRE}' (MI018) creado.")
    else:
        print(f"Producto '{prod105.PROD_NOMBRE}' (MI018) ya existía.")
        print(f"Producto '{prod105.PROD_NOMBRE}' (MI018) no se actualizó el gramaje.")

    prod106, created = Producto.objects.update_or_create(
        ID_PRODUCTO="MI019",
        defaults={
        'PROD_CATEGORIA':cat5,
        'PROD_NOMBRE':"MAGNESIO / ZINC / POTASIO",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':210.00,
        'PROD_PRECIO_PUB':264.00,
        }
    )
    if created:
        print(f"Producto '{prod106.PROD_NOMBRE}' (MI019) creado.")
    else:
        print(f"Producto '{prod106.PROD_NOMBRE}' (MI019) ya existía.")
        print(f"Producto '{prod106.PROD_NOMBRE}' (MI019) no se actualizó el gramaje.")
    
    prod107, created = Producto.objects.update_or_create(
        ID_PRODUCTO="MI020",
        defaults={
        'PROD_CATEGORIA':cat5,
        'PROD_NOMBRE':"MAGNESIO (Treonato)",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':304.00,
        'PROD_PRECIO_PUB':380.00,
        'PROD_GRAMAJE':750.00
        }
    )
    if created:
        print(f"Producto '{prod107.PROD_NOMBRE}' (MI020) creado.")
    else:
        print(f"Producto '{prod107.PROD_NOMBRE}' (MI020) ya existía. Actualizando gramaje.")
        prod107.PROD_GRAMAJE = 750.00
        prod107.save()
        print(f"Producto '{prod107.PROD_NOMBRE}' (MI020) actualizado con gramaje.")

    prod108, created = Producto.objects.update_or_create(
        ID_PRODUCTO="MI021",
        defaults={
        'PROD_CATEGORIA':cat5,
        'PROD_NOMBRE':"MAGNESIO (Treonato)",
        'CONTENIDO_PZS':"160 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':450.00,
        'PROD_PRECIO_PUB':560.00,
        'PROD_GRAMAJE':750.00
        }
    )
    if created:
        print(f"Producto '{prod108.PROD_NOMBRE}' (MI021) creado.")
    else:
        print(f"Producto '{prod108.PROD_NOMBRE}' (MI021) ya existía. Actualizando gramaje.")
        prod108.PROD_GRAMAJE = 750.00
        prod108.save()
        print(f"Producto '{prod108.PROD_NOMBRE}' (MI021) actualizado con gramaje.")

    # SUPLEMENTOS EN POLVO

    prod109, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP001",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"GOLDEN MILK (Bebida de Coco con Curcuma)",
        'CONTENIDO_PZS':"450 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':164.00,
        'PROD_PRECIO_PUB':192.00,
        'PROD_GRAMAJE':450.00
        }
    )
    if created:
        print(f"Producto '{prod109.PROD_NOMBRE}' (SP001) creado.")
    else:
        print(f"Producto '{prod109.PROD_NOMBRE}' (SP001) ya existía. Actualizando gramaje.")
        prod109.PROD_GRAMAJE = 450.00
        prod109.save()
        print(f"Producto '{prod109.PROD_NOMBRE}' (SP001) actualizado con gramaje.")

    prod110, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP002",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"GOLDEN MILK (Bebida de Coco con Curcuma)",
        'CONTENIDO_PZS':"1100 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':324.00,
        'PROD_PRECIO_PUB':380.00,
        'PROD_GRAMAJE':1100.00
        }
    )
    if created:
        print(f"Producto '{prod110.PROD_NOMBRE}' (SP002) creado.")
    else:
        print(f"Producto '{prod110.PROD_NOMBRE}' (SP002) ya existía. Actualizando gramaje.")
        prod110.PROD_GRAMAJE = 1100.00
        prod110.save()
        print(f"Producto '{prod110.PROD_NOMBRE}' (SP002) actualizado con gramaje.")

    prod111, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP003",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"MATCHA con jugo de limon",
        'CONTENIDO_PZS':"400 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':220.00,
        'PROD_PRECIO_PUB':260.00,
        'PROD_GRAMAJE':400.00
        }
    )
    if created:
        print(f"Producto '{prod111.PROD_NOMBRE}' (SP003) creado.")
    else:
        print(f"Producto '{prod111.PROD_NOMBRE}' (SP003) ya existía. Actualizando gramaje.")
        prod111.PROD_GRAMAJE = 400.00
        prod111.save()
        print(f"Producto '{prod111.PROD_NOMBRE}' (SP003) actualizado con gramaje.")

    prod112, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP004",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE': "NEW WOMAN FRESA",
        'CONTENIDO_PZS':"400 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':280.00,
        'PROD_PRECIO_PUB':360.00,
        'PROD_GRAMAJE':400.00
        }
    )
    if created:
        print(f"Producto '{prod112.PROD_NOMBRE}' (SP004) creado.")
    else:
        print(f"Producto '{prod112.PROD_NOMBRE}' (SP004) ya existía. Actualizando gramaje.")
        prod112.PROD_GRAMAJE = 400.00
        prod112.save()
        print(f"Producto '{prod112.PROD_NOMBRE}' (SP004) actualizado con gramaje.")

    prod113, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP005",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"NEW WOMAN FRESA",
        'CONTENIDO_PZS':"800 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':450.00,
        'PROD_PRECIO_PUB':550.00,
        'PROD_GRAMAJE':800.00
        }
    )
    if created:
        print(f"Producto '{prod113.PROD_NOMBRE}' (SP005) creado.")
    else:
        print(f"Producto '{prod113.PROD_NOMBRE}' (SP005) ya existía. Actualizando gramaje.")
        prod113.PROD_GRAMAJE = 800.00
        prod113.save()
        print(f"Producto '{prod113.PROD_NOMBRE}' (SP005) actualizado con gramaje.")

    prod114, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP006",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"NEW WOMAN VAINILLA",
        'CONTENIDO_PZS':"400 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':280.00,
        'PROD_PRECIO_PUB':360.00,
        'PROD_GRAMAJE':400.00
        }
    )
    if created:
        print(f"Producto '{prod114.PROD_NOMBRE}' (SP006) creado.")
    else:
        print(f"Producto '{prod114.PROD_NOMBRE}' (SP006) ya existía. Actualizando gramaje.")
        prod114.PROD_GRAMAJE = 400.00
        prod114.save()
        print(f"Producto '{prod114.PROD_NOMBRE}' (SP006) actualizado con gramaje.")

    prod115, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP007",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"NEW WOMAN VAINILLA",
        'CONTENIDO_PZS':"800 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':450.00,
        'PROD_PRECIO_PUB':550.00,
        'PROD_GRAMAJE':800.00
        }
    )
    if created:
        print(f"Producto '{prod115.PROD_NOMBRE}' (SP007) creado.")
    else:
        print(f"Producto '{prod115.PROD_NOMBRE}' (SP007) ya existía. Actualizando gramaje.")
        prod115.PROD_GRAMAJE = 800.00
        prod115.save()
        print(f"Producto '{prod115.PROD_NOMBRE}' (SP007) actualizado con gramaje.")

    prod116, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP008",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"NEW WOMAN CHOCOLATE",
        'CONTENIDO_PZS':"400 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':280.00,
        'PROD_PRECIO_PUB':360.00,
        'PROD_GRAMAJE':400.00
        }
    )
    if created:
        print(f"Producto '{prod116.PROD_NOMBRE}' (SP008) creado.")
    else:
        print(f"Producto '{prod116.PROD_NOMBRE}' (SP008) ya existía. Actualizando gramaje.")
        prod116.PROD_GRAMAJE = 400.00
        prod116.save()
        print(f"Producto '{prod116.PROD_NOMBRE}' (SP008) actualizado con gramaje.")

    prod117, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP009",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"NEW WOMAN CHOCOLATE",
        'CONTENIDO_PZS':"800 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':450.00,
        'PROD_PRECIO_PUB':550.00,
        'PROD_GRAMAJE':800.00
        }
    )
    if created:
        print(f"Producto '{prod117.PROD_NOMBRE}' (SP009) creado.")
    else:
        print(f"Producto '{prod117.PROD_NOMBRE}' (SP009) ya existía. Actualizando gramaje.")
        prod117.PROD_GRAMAJE = 800.00
        prod117.save()
        print(f"Producto '{prod117.PROD_NOMBRE}' (SP009) actualizado con gramaje.")

    prod118, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP010",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"OSTEOPROTEC FRESA",
        'CONTENIDO_PZS':"400 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':304.00,
        'PROD_PRECIO_PUB':380.00,
        'PROD_GRAMAJE':400.00
        }
    )
    if created:
        print(f"Producto '{prod118.PROD_NOMBRE}' (SP010) creado.")
    else:
        print(f"Producto '{prod118.PROD_NOMBRE}' (SP010) ya existía. Actualizando gramaje.")
        prod118.PROD_GRAMAJE = 400.00
        prod118.save()
        print(f"Producto '{prod118.PROD_NOMBRE}' (SP010) actualizado con gramaje.")

    prod119, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP011",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"OSTEOPROTEC FRESA",
        'CONTENIDO_PZS':"800 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':464.00,
        'PROD_PRECIO_PUB':560.00,
        'PROD_GRAMAJE':800.00
        }
    )
    if created:
        print(f"Producto '{prod119.PROD_NOMBRE}' (SP011) creado.")
    else:
        print(f"Producto '{prod119.PROD_NOMBRE}' (SP011) ya existía. Actualizando gramaje.")
        prod119.PROD_GRAMAJE = 800.00
        prod119.save()
        print(f"Producto '{prod119.PROD_NOMBRE}' (SP011) actualizado con gramaje.")

    prod120, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP012",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"OSTEOPROTEC VAINILLA",
        'CONTENIDO_PZS':"400 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':304.00,
        'PROD_PRECIO_PUB':380.00,
        'PROD_GRAMAJE':400.00
        }
    )
    if created:
        print(f"Producto '{prod120.PROD_NOMBRE}' (SP012) creado.")
    else:
        print(f"Producto '{prod120.PROD_NOMBRE}' (SP012) ya existía. Actualizando gramaje.")
        prod120.PROD_GRAMAJE = 400.00
        prod120.save()
        print(f"Producto '{prod120.PROD_NOMBRE}' (SP012) actualizado con gramaje.")

    prod121, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP013",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"OSTEOPROTEC VAINILLA",
        'CONTENIDO_PZS':"800 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':464.00,
        'PROD_PRECIO_PUB':560.00,
        'PROD_GRAMAJE':800.00
        }
    )
    if created:
        print(f"Producto '{prod121.PROD_NOMBRE}' (SP013) creado.")
    else:
        print(f"Producto '{prod121.PROD_NOMBRE}' (SP013) ya existía. Actualizando gramaje.")
        prod121.PROD_GRAMAJE = 800.00
        prod121.save()
        print(f"Producto '{prod121.PROD_NOMBRE}' (SP013) actualizado con gramaje.")

    prod123, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP014",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"OSTEOPROTEC CHOCOLATE",
        'CONTENIDO_PZS':"400 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':304.00,
        'PROD_PRECIO_PUB':380.00,
        'PROD_GRAMAJE':400.00
        }
    )
    if created:
        print(f"Producto '{prod123.PROD_NOMBRE}' (SP014) creado.")
    else:
        print(f"Producto '{prod123.PROD_NOMBRE}' (SP014) ya existía. Actualizando gramaje.")
        prod123.PROD_GRAMAJE = 400.00
        prod123.save()
        print(f"Producto '{prod123.PROD_NOMBRE}' (SP014) actualizado con gramaje.")

    prod124, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP015",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"OSTEOPROTEC CHOCOLATE",
        'CONTENIDO_PZS':"800 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':464.00,
        'PROD_PRECIO_PUB':560.00,
        'PROD_GRAMAJE':800.00
        }
    )
    if created:
        print(f"Producto '{prod124.PROD_NOMBRE}' (SP015) creado.")
    else:
        print(f"Producto '{prod124.PROD_NOMBRE}' (SP015) ya existía. Actualizando gramaje.")
        prod124.PROD_GRAMAJE = 800.00
        prod124.save()
        print(f"Producto '{prod124.PROD_NOMBRE}' (SP015) actualizado con gramaje.")

    prod125, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP022",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"SOYA KIDS FRESA",
        'CONTENIDO_PZS':"500 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':182.00,
        'PROD_PRECIO_PUB':220.00,
        'PROD_GRAMAJE':500.00
        }
    )
    if created:
        print(f"Producto '{prod125.PROD_NOMBRE}' (SP022) creado.")
    else:
        print(f"Producto '{prod125.PROD_NOMBRE}' (SP022) ya existía. Actualizando gramaje.")
        prod125.PROD_GRAMAJE = 500.00
        prod125.save()
        print(f"Producto '{prod125.PROD_NOMBRE}' (SP022) actualizado con gramaje.")

    prod126, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP023",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"SOYA KIDS FRESA",
        'CONTENIDO_PZS':"900 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':280.00,
        'PROD_PRECIO_PUB':330.00,
        'PROD_GRAMAJE':900.00
        }
    )
    if created:
        print(f"Producto '{prod126.PROD_NOMBRE}' (SP023) creado.")
    else:
        print(f"Producto '{prod126.PROD_NOMBRE}' (SP023) ya existía. Actualizando gramaje.")
        prod126.PROD_GRAMAJE = 900.00
        prod126.save()
        print(f"Producto '{prod126.PROD_NOMBRE}' (SP023) actualizado con gramaje.")

    prod127, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP024",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"SOYA KIDS VAINILLA",
        'CONTENIDO_PZS':"500 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':182.00,
        'PROD_PRECIO_PUB':220.00,
        'PROD_GRAMAJE':500.00
        }
    )
    if created:
        print(f"Producto '{prod127.PROD_NOMBRE}' (SP024) creado.")
    else:
        print(f"Producto '{prod127.PROD_NOMBRE}' (SP024) ya existía. Actualizando gramaje.")
        prod127.PROD_GRAMAJE = 500.00
        prod127.save()
        print(f"Producto '{prod127.PROD_NOMBRE}' (SP024) actualizado con gramaje.")

    prod128, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP025",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"SOYA KIDS VAINILLA",
        'CONTENIDO_PZS':"900 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':280.00,
        'PROD_PRECIO_PUB':330.00,
        'PROD_GRAMAJE':900.00
        }
    )
    if created:
        print(f"Producto '{prod128.PROD_NOMBRE}' (SP025) creado.")
    else:
        print(f"Producto '{prod128.PROD_NOMBRE}' (SP025) ya existía. Actualizando gramaje.")
        prod128.PROD_GRAMAJE = 900.00
        prod128.save()
        print(f"Producto '{prod128.PROD_NOMBRE}' (SP025) actualizado con gramaje.")

    prod129, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP026",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"SOYA KIDS CHOCOLATE",
        'CONTENIDO_PZS':"500 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':182.00,
        'PROD_PRECIO_PUB':220.00,
        'PROD_GRAMAJE':500.00
        }
    )
    if created:
        print(f"Producto '{prod129.PROD_NOMBRE}' (SP026) creado.")
    else:
        print(f"Producto '{prod129.PROD_NOMBRE}' (SP026) ya existía. Actualizando gramaje.")
        prod129.PROD_GRAMAJE = 500.00
        prod129.save()
        print(f"Producto '{prod129.PROD_NOMBRE}' (SP026) actualizado con gramaje.")

    prod130, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP027",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"SOYA KIDS CHOCOLATE",
        'CONTENIDO_PZS':"900 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':280.00,
        'PROD_PRECIO_PUB':330.00,
        'PROD_GRAMAJE':900.00
        }
    )
    if created:
        print(f"Producto '{prod130.PROD_NOMBRE}' (SP027) creado.")
    else:
        print(f"Producto '{prod130.PROD_NOMBRE}' (SP027) ya existía. Actualizando gramaje.")
        prod130.PROD_GRAMAJE = 900.00
        prod130.save()
        print(f"Producto '{prod130.PROD_NOMBRE}' (SP027) actualizado con gramaje.")

    prod131, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP032",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"CURCUMA ORIENTAL con Especias y Leche de Coco",
        'CONTENIDO_PZS':"450 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':172.00,
        'PROD_PRECIO_PUB':236.00,
        'PROD_GRAMAJE':450.00
        }
    )
    if created:
        print(f"Producto '{prod131.PROD_NOMBRE}' (SP032) creado.")
    else:
        print(f"Producto '{prod131.PROD_NOMBRE}' (SP032) ya existía. Actualizando gramaje.")
        prod131.PROD_GRAMAJE = 450.00
        prod131.save()
        print(f"Producto '{prod131.PROD_NOMBRE}' (SP032) actualizado con gramaje.")

    prod132, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP033",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"CURCUMA ORIENTAL con Especias y Leche de Coco",
        'CONTENIDO_PZS':"1100 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':550.00,
        'PROD_PRECIO_PUB':650.00,
        'PROD_GRAMAJE':1100.00
        }
    )
    if created:
        print(f"Producto '{prod132.PROD_NOMBRE}' (SP033) creado.")
    else:
        print(f"Producto '{prod132.PROD_NOMBRE}' (SP033) ya existía. Actualizando gramaje.")
        prod132.PROD_GRAMAJE = 1100.00
        prod132.save()
        print(f"Producto '{prod132.PROD_NOMBRE}' (SP033) actualizado con gramaje.")

    prod133, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP0321",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"PREBIOTIC FIBER CITRUS LEMON",
        'CONTENIDO_PZS':"400 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':310.00,
        'PROD_PRECIO_PUB':380.00,
        'PROD_GRAMAJE':400.00
        }
    )
    if created:
        print(f"Producto '{prod133.PROD_NOMBRE}' (SP0321) creado.")
    else:
        print(f"Producto '{prod133.PROD_NOMBRE}' (SP0321) ya existía. Actualizando gramaje.")
        prod133.PROD_GRAMAJE = 400.00
        prod133.save()
        print(f"Producto '{prod133.PROD_NOMBRE}' (SP0321) actualizado con gramaje.")

    prod134, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP0331",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"PREBIOTIC FIBER CITRUS LEMON",
        'CONTENIDO_PZS':"800 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':550.00,
        'PROD_PRECIO_PUB':650.00,
        'PROD_GRAMAJE':800.00
        }
    )
    if created:
        print(f"Producto '{prod134.PROD_NOMBRE}' (SP0331) creado.")
    else:
        print(f"Producto '{prod134.PROD_NOMBRE}' (SP0331) ya existía. Actualizando gramaje.")
        prod134.PROD_GRAMAJE = 800.00
        prod134.save()
        print(f"Producto '{prod134.PROD_NOMBRE}' (SP0331) actualizado con gramaje.")

    prod135, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP034",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"PREBIOTIC FIBER CITRUS ORANGE",
        'CONTENIDO_PZS':"400 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':310.00,
        'PROD_PRECIO_PUB':380.00,
        'PROD_GRAMAJE':400.00
        }
    )
    if created:
        print(f"Producto '{prod135.PROD_NOMBRE}' (SP034) creado.")
    else:
        print(f"Producto '{prod135.PROD_NOMBRE}' (SP034) ya existía. Actualizando gramaje.")
        prod135.PROD_GRAMAJE = 400.00
        prod135.save()
        print(f"Producto '{prod135.PROD_NOMBRE}' (SP034) actualizado con gramaje.")

    prod136, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP035",
        defaults={
        'PROD_CATEGORIA':cat6,
        'PROD_NOMBRE':"PREBIOTIC FIBER CITRUS ORANGE",
        'CONTENIDO_PZS':"800 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':550.00,
        'PROD_PRECIO_PUB':650.00,
        'PROD_GRAMAJE':800.00
        }
    )
    if created:
        print(f"Producto '{prod136.PROD_NOMBRE}' (SP035) creado.")
    else:
        print(f"Producto '{prod136.PROD_NOMBRE}' (SP035) ya existía. Actualizando gramaje.")
        prod136.PROD_GRAMAJE = 800.00
        prod136.save()
        print(f"Producto '{prod136.PROD_NOMBRE}' (SP035) actualizado con gramaje.")


    # PROTEÍNAS
    prod137, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SPR006",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"KETO PURE ISOLATE WPI PROTEIN ZERO CARB VAINILLA",
        'CONTENIDO_PZS':"1100 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':1250.00,
        'PROD_PRECIO_PUB':1450.00,
        'PROD_GRAMAJE':1100.00
        }
    )
    if created:
        print(f"Producto '{prod137.PROD_NOMBRE}' (SPR006) creado.")
    else:
        print(f"Producto '{prod137.PROD_NOMBRE}' (SPR006) ya existía. Actualizando gramaje.")
        prod137.PROD_GRAMAJE = 1100.00
        prod137.save()
        print(f"Producto '{prod137.PROD_NOMBRE}' (SPR006) actualizado con gramaje.")

    prod138, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SPR007",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"KETO PURE ISOLATE WPI PROTEIN ZERO CARB TARO",
        'CONTENIDO_PZS':"1100 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':1250.00,
        'PROD_PRECIO_PUB':1450.00,
        'PROD_GRAMAJE':1100.00
        }
    )
    if created:
        print(f"Producto '{prod138.PROD_NOMBRE}' (SPR007) creado.")
    else:
        print(f"Producto '{prod138.PROD_NOMBRE}' (SPR007) ya existía. Actualizando gramaje.")
        prod138.PROD_GRAMAJE = 1100.00
        prod138.save()
        print(f"Producto '{prod138.PROD_NOMBRE}' (SPR007) actualizado con gramaje.")

    prod139, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SPR008",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"KETO PURE ISOLATE WPI PROTEIN ZERO CARB COCOA",
        'CONTENIDO_PZS':"1100 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':1250.00,
        'PROD_PRECIO_PUB':1450.00,
        'PROD_GRAMAJE':1100.00
        }
    )
    if created:
        print(f"Producto '{prod139.PROD_NOMBRE}' (SPR008) creado.")
    else:
        print(f"Producto '{prod139.PROD_NOMBRE}' (SPR008) ya existía. Actualizando gramaje.")
        prod139.PROD_GRAMAJE = 1100.00
        prod139.save()
        print(f"Producto '{prod139.PROD_NOMBRE}' (SPR008) actualizado con gramaje.")

    prod140, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SPR009",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"KETO PURE ISOLATE WPI PROTEIN ZERO CARB CAPUCHINO",
        'CONTENIDO_PZS':"1100 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':1250.00,
        'PROD_PRECIO_PUB':1450.00,
        'PROD_GRAMAJE':1100.00
        }
    )
    if created:
        print(f"Producto '{prod140.PROD_NOMBRE}' (SPR009) creado.")
    else:
        print(f"Producto '{prod140.PROD_NOMBRE}' (SPR009) ya existía. Actualizando gramaje.")
        prod140.PROD_GRAMAJE = 1100.00
        prod140.save()
        print(f"Producto '{prod140.PROD_NOMBRE}' (SPR009) actualizado con gramaje.")

    prod141, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SPR010",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"KETO PURE ISOLATE WPI PROTEIN ZERO CARB FRESA",
        'CONTENIDO_PZS':"1100 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':1250.00,
        'PROD_PRECIO_PUB':1450.00,
        'PROD_GRAMAJE':1100.00
        }
    )
    if created:
        print(f"Producto '{prod141.PROD_NOMBRE}' (SPR010) creado.")
    else:
        print(f"Producto '{prod141.PROD_NOMBRE}' (SPR010) ya existía. Actualizando gramaje.")
        prod141.PROD_GRAMAJE = 1100.00
        prod141.save()
        print(f"Producto '{prod141.PROD_NOMBRE}' (SPR010) actualizado con gramaje.")

    prod142, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SPR011",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"PROTEINA DE SOYA 95% NATURAL",
        'CONTENIDO_PZS':"460 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':292.00,
        'PROD_PRECIO_PUB':360.00,
        'PROD_GRAMAJE':460.00
        }
    )
    if created:
        print(f"Producto '{prod142.PROD_NOMBRE}' (SPR011) creado.")
    else:
        print(f"Producto '{prod142.PROD_NOMBRE}' (SPR011) ya existía. Actualizando gramaje.")
        prod142.PROD_GRAMAJE = 460.00
        prod142.save()
        print(f"Producto '{prod142.PROD_NOMBRE}' (SPR011) actualizado con gramaje.")

    prod143, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SPR012",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"PROTEINA DE SOYA 95% CHOCOLATE",
        'CONTENIDO_PZS':"460 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':310.00,
        'PROD_PRECIO_PUB':380.00,
        'PROD_GRAMAJE':460.00
        }
    )
    if created:
        print(f"Producto '{prod143.PROD_NOMBRE}' (SPR012) creado.")
    else:
        print(f"Producto '{prod143.PROD_NOMBRE}' (SPR012) ya existía. Actualizando gramaje.")
        prod143.PROD_GRAMAJE = 460.00
        prod143.save()
        print(f"Producto '{prod143.PROD_NOMBRE}' (SPR012) actualizado con gramaje.")

    prod144, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SPR013",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"PROTEINA DE SOYA 95% FRESA",
        'CONTENIDO_PZS':"460 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':310.00,
        'PROD_PRECIO_PUB':380.00,
        'PROD_GRAMAJE':460.00
        }
    )
    if created:
        print(f"Producto '{prod144.PROD_NOMBRE}' (SPR013) creado.")
    else:
        print(f"Producto '{prod144.PROD_NOMBRE}' (SPR013) ya existía. Actualizando gramaje.")
        prod144.PROD_GRAMAJE = 460.00
        prod144.save()
        print(f"Producto '{prod144.PROD_NOMBRE}' (SPR013) actualizado con gramaje.")

    prod145, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SPR014",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"PROTEINA DE SOYA 95% VAINILLA",
        'CONTENIDO_PZS':"460 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':310.00,
        'PROD_PRECIO_PUB':380.00,
        'PROD_GRAMAJE':460.00
        }
    )
    if created:
        print(f"Producto '{prod145.PROD_NOMBRE}' (SPR014) creado.")
    else:
        print(f"Producto '{prod145.PROD_NOMBRE}' (SPR014) ya existía. Actualizando gramaje.")
        prod145.PROD_GRAMAJE = 460.00
        prod145.save()
        print(f"Producto '{prod145.PROD_NOMBRE}' (SPR014) actualizado con gramaje.")

    prod146, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SPR015",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"PROTEINA DE SOYA 95% NATURAL",
        'CONTENIDO_PZS':"1100 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':624.00,
        'PROD_PRECIO_PUB':780.00,
        'PROD_GRAMAJE':1100.00
        }
    )
    if created:
        print(f"Producto '{prod146.PROD_NOMBRE}' (SPR015) creado.")
    else:
        print(f"Producto '{prod146.PROD_NOMBRE}' (SPR015) ya existía. Actualizando gramaje.")
        prod146.PROD_GRAMAJE = 1100.00
        prod146.save()
        print(f"Producto '{prod146.PROD_NOMBRE}' (SPR015) actualizado con gramaje.")

    prod147, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SPR016",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"PROTEINA DE SOYA 95% CHOCOLATE",
        'CONTENIDO_PZS':"1100 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':650.00,
        'PROD_PRECIO_PUB':820.00,
        'PROD_GRAMAJE':1100.00
        }
    )
    if created:
        print(f"Producto '{prod147.PROD_NOMBRE}' (SPR016) creado.")
    else:
        print(f"Producto '{prod147.PROD_NOMBRE}' (SPR016) ya existía. Actualizando gramaje.")
        prod147.PROD_GRAMAJE = 1100.00
        prod147.save()
        print(f"Producto '{prod147.PROD_NOMBRE}' (SPR016) actualizado con gramaje.")

    prod148, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SPR017",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"PROTEINA DE SOYA 95% FRESA",
        'CONTENIDO_PZS':"1100 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':650.00,
        'PROD_PRECIO_PUB':820.00,
        'PROD_GRAMAJE':1100.00
        }
    )
    if created:
        print(f"Producto '{prod148.PROD_NOMBRE}' (SPR017) creado.")
    else:
        print(f"Producto '{prod148.PROD_NOMBRE}' (SPR017) ya existía. Actualizando gramaje.")
        prod148.PROD_GRAMAJE = 1100.00
        prod148.save()
        print(f"Producto '{prod148.PROD_NOMBRE}' (SPR017) actualizado con gramaje.")

    prod149, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SPR018",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"PROTEINA DE SOYA 95% VAINILLA",
        'CONTENIDO_PZS':"1100 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':650.00,
        'PROD_PRECIO_PUB':820.00,
        'PROD_GRAMAJE':1100.00
        }
    )
    if created:
        print(f"Producto '{prod149.PROD_NOMBRE}' (SPR018) creado.")
    else:
        print(f"Producto '{prod149.PROD_NOMBRE}' (SPR018) ya existía. Actualizando gramaje.")
        prod149.PROD_GRAMAJE = 1100.00
        prod149.save()
        print(f"Producto '{prod149.PROD_NOMBRE}' (SPR018) actualizado con gramaje.")

    prod150, created = Producto.objects.update_or_create(
        ID_PRODUCTO="COMP028",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"PROTE MILK",
        'CONTENIDO_PZS':"400 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':104.00,
        'PROD_PRECIO_PUB':130.00,
        'PROD_GRAMAJE':400.00
        }
    )
    if created:
        print(f"Producto '{prod150.PROD_NOMBRE}' (COMP028) creado.")
    else:
        print(f"Producto '{prod150.PROD_NOMBRE}' (COMP028) ya existía. Actualizando gramaje.")
        prod150.PROD_GRAMAJE = 400.00
        prod150.save()
        print(f"Producto '{prod150.PROD_NOMBRE}' (COMP028) actualizado con gramaje.")

    prod151, created = Producto.objects.update_or_create(
        ID_PRODUCTO="COMP029",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"PROTE MILK",
        'CONTENIDO_PZS':"800 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':184.00,
        'PROD_PRECIO_PUB':230.00,
        'PROD_GRAMAJE':800.00
        }
    )
    if created:
        print(f"Producto '{prod151.PROD_NOMBRE}' (COMP029) creado.")
    else:
        print(f"Producto '{prod151.PROD_NOMBRE}' (COMP029) ya existía. Actualizando gramaje.")
        prod151.PROD_GRAMAJE = 800.00
        prod151.save()
        print(f"Producto '{prod151.PROD_NOMBRE}' (COMP029) actualizado con gramaje.")

    prod152, created = Producto.objects.update_or_create(
        ID_PRODUCTO="COMP030",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"SUPRA MILK",
        'CONTENIDO_PZS':"400 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':115.00,
        'PROD_PRECIO_PUB':145.00,
        'PROD_GRAMAJE':400.00
        }
    )
    if created:
        print(f"Producto '{prod152.PROD_NOMBRE}' (COMP030) creado.")
    else:
        print(f"Producto '{prod152.PROD_NOMBRE}' (COMP030) ya existía. Actualizando gramaje.")
        prod152.PROD_GRAMAJE = 400.00
        prod152.save()
        print(f"Producto '{prod152.PROD_NOMBRE}' (COMP030) actualizado con gramaje.")

    prod153, created = Producto.objects.update_or_create(
        ID_PRODUCTO="COMP031",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"SUPRA MILK",
        'CONTENIDO_PZS':"800 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':202.00,
        'PROD_PRECIO_PUB':254.00,
        'PROD_GRAMAJE':800.00
        }
    )
    if created:
        print(f"Producto '{prod153.PROD_NOMBRE}' (COMP031) creado.")
    else:
        print(f"Producto '{prod153.PROD_NOMBRE}' (COMP031) ya existía. Actualizando gramaje.")
        prod153.PROD_GRAMAJE = 800.00
        prod153.save()
        print(f"Producto '{prod153.PROD_NOMBRE}' (COMP031) actualizado con gramaje.")

    prod154, created = Producto.objects.update_or_create(
        ID_PRODUCTO="PR019",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"VEGAN PROTEIN PREMIUM COCOA",
        'CONTENIDO_PZS':"840 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':624.00,
        'PROD_PRECIO_PUB':740.00,
        'PROD_GRAMAJE':840.00
        }
    )
    if created:
        print(f"Producto '{prod154.PROD_NOMBRE}' (PR019) creado.")
    else:
        print(f"Producto '{prod154.PROD_NOMBRE}' (PR019) ya existía. Actualizando gramaje.")
        prod154.PROD_GRAMAJE = 840.00
        prod154.save()
        print(f"Producto '{prod154.PROD_NOMBRE}' (PR019) actualizado con gramaje.")

    prod155, created = Producto.objects.update_or_create(
        ID_PRODUCTO="PR020",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"VEGAN PROTEIN PREMIUM VAINILLA",
        'CONTENIDO_PZS':"840 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':624.00,
        'PROD_PRECIO_PUB':740.00,
        'PROD_GRAMAJE':840.00
        }
    )
    if created:
        print(f"Producto '{prod155.PROD_NOMBRE}' (PR020) creado.")
    else:
        print(f"Producto '{prod155.PROD_NOMBRE}' (PR020) ya existía. Actualizando gramaje.")
        prod155.PROD_GRAMAJE = 840.00
        prod155.save()
        print(f"Producto '{prod155.PROD_NOMBRE}' (PR020) actualizado con gramaje.")

    prod156, created = Producto.objects.update_or_create(
        ID_PRODUCTO="PR021",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"VEGAN PROTEIN PREMIUM FRUTOS ROJOS",
        'CONTENIDO_PZS':"840 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':624.00,
        'PROD_PRECIO_PUB':740.00,
        'PROD_GRAMAJE':840.00
        }
    )
    if created:
        print(f"Producto '{prod156.PROD_NOMBRE}' (PR021) creado.")
    else:
        print(f"Producto '{prod156.PROD_NOMBRE}' (PR021) ya existía. Actualizando gramaje.")
        prod156.PROD_GRAMAJE = 840.00
        prod156.save()
        print(f"Producto '{prod156.PROD_NOMBRE}' (PR021) actualizado con gramaje.")

    prod157, created = Producto.objects.update_or_create(
        ID_PRODUCTO="PR022",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"VEGAN PROTEIN PREMIUM CHAI",
        'CONTENIDO_PZS':"840 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':624.00,
        'PROD_PRECIO_PUB':740.00,
        'PROD_GRAMAJE':840.00
        }
    )
    if created:
        print(f"Producto '{prod157.PROD_NOMBRE}' (PR022) creado.")
    else:
        print(f"Producto '{prod157.PROD_NOMBRE}' (PR022) ya existía. Actualizando gramaje.")
        prod157.PROD_GRAMAJE = 840.00
        prod157.save()
        print(f"Producto '{prod157.PROD_NOMBRE}' (PR022) actualizado con gramaje.")

    prod158, created = Producto.objects.update_or_create(
        ID_PRODUCTO="PR023",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"ISOLATE WHEY PROTEIN STRAWBERRY",
        'CONTENIDO_PZS':"1100 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':1050.00,
        'PROD_PRECIO_PUB':1200.00,
        'PROD_GRAMAJE':1100.00
        }
    )
    if created:
        print(f"Producto '{prod158.PROD_NOMBRE}' (PR023) creado.")
    else:
        print(f"Producto '{prod158.PROD_NOMBRE}' (PR023) ya existía. Actualizando gramaje.")
        prod158.PROD_GRAMAJE = 1100.00
        prod158.save()
        print(f"Producto '{prod158.PROD_NOMBRE}' (PR023) actualizado con gramaje.")

    prod159, created = Producto.objects.update_or_create(
        ID_PRODUCTO="PR024",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"ISOLATE WHEY PROTEIN CHOCOLATE",
        'CONTENIDO_PZS':"1100 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':1050.00,
        'PROD_PRECIO_PUB':1200.00,
        'PROD_GRAMAJE':1100.00
        }
    )
    if created:
        print(f"Producto '{prod159.PROD_NOMBRE}' (PR024) creado.")
    else:
        print(f"Producto '{prod159.PROD_NOMBRE}' (PR024) ya existía. Actualizando gramaje.")
        prod159.PROD_GRAMAJE = 1100.00
        prod159.save()
        print(f"Producto '{prod159.PROD_NOMBRE}' (PR024) actualizado con gramaje.")

    prod160, created = Producto.objects.update_or_create(
        ID_PRODUCTO="PR025",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"ISOLATE WHEY PROTEIN VAINILLA",
        'CONTENIDO_PZS':"1100 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':1050.00,
        'PROD_PRECIO_PUB':1200.00,
        'PROD_GRAMAJE':1100.00
        }
    )
    if created:
        print(f"Producto '{prod160.PROD_NOMBRE}' (PR025) creado.")
    else:
        print(f"Producto '{prod160.PROD_NOMBRE}' (PR025) ya existía. Actualizando gramaje.")
        prod160.PROD_GRAMAJE = 1100.00
        prod160.save()
        print(f"Producto '{prod160.PROD_NOMBRE}' (PR025) actualizado con gramaje.")

    prod161, created = Producto.objects.update_or_create(
        ID_PRODUCTO="PR026",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"ISOLATE WHEY PROTEIN MOKACCINO",
        'CONTENIDO_PZS':"1100 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':1050.00,
        'PROD_PRECIO_PUB':1200.00,
        'PROD_GRAMAJE':1100.00
        }
    )
    if created:
        print(f"Producto '{prod161.PROD_NOMBRE}' (PR026) creado.")
    else:
        print(f"Producto '{prod161.PROD_NOMBRE}' (PR026) ya existía. Actualizando gramaje.")
        prod161.PROD_GRAMAJE = 1100.00
        prod161.save()
        print(f"Producto '{prod161.PROD_NOMBRE}' (PR026) actualizado con gramaje.")

    prod162, created = Producto.objects.update_or_create(
        ID_PRODUCTO="PR031",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"100% WHEY PROTEIN CONCENTRATE MOKACCINO",
        'CONTENIDO_PZS':"900 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':740.00,
        'PROD_PRECIO_PUB':860.00,
        'PROD_GRAMAJE':900.00
        }
    )
    if created:
        print(f"Producto '{prod162.PROD_NOMBRE}' (PR031) creado.")
    else:
        print(f"Producto '{prod162.PROD_NOMBRE}' (PR031) ya existía. Actualizando gramaje.")
        prod162.PROD_GRAMAJE = 900.00
        prod162.save()
        print(f"Producto '{prod162.PROD_NOMBRE}' (PR031) actualizado con gramaje.")

    prod163, created = Producto.objects.update_or_create(
        ID_PRODUCTO="PR032",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"100% WHEY PROTEIN CONCENTRATE VAINILLA",
        'CONTENIDO_PZS':"900 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':740.00,
        'PROD_PRECIO_PUB':860.00,
        'PROD_GRAMAJE':900.00
        }
    )
    if created:
        print(f"Producto '{prod163.PROD_NOMBRE}' (PR032) creado.")
    else:
        print(f"Producto '{prod163.PROD_NOMBRE}' (PR032) ya existía. Actualizando gramaje.")
        prod163.PROD_GRAMAJE = 900.00
        prod163.save()
        print(f"Producto '{prod163.PROD_NOMBRE}' (PR032) actualizado con gramaje.")

    prod164, created = Producto.objects.update_or_create(
        ID_PRODUCTO="PR033",
        defaults={
        'PROD_CATEGORIA':cat7,
        'PROD_NOMBRE':"100% WHEY PROTEIN CONCENTRATE STRAWBERRY",
        'CONTENIDO_PZS':"900 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':740.00,
        'PROD_PRECIO_PUB':860.00,
        'PROD_GRAMAJE':900.00
        }
    )
    if created:
        print(f"Producto '{prod164.PROD_NOMBRE}' (PR033) creado.")
    else:
        print(f"Producto '{prod164.PROD_NOMBRE}' (PR033) ya existía. Actualizando gramaje.")
        prod164.PROD_GRAMAJE = 900.00
        prod164.save()
        print(f"Producto '{prod164.PROD_NOMBRE}' (PR033) actualizado con gramaje.")


    # COLAGENOS
    prod165, created = Producto.objects.update_or_create(
        ID_PRODUCTO="CO001",
        defaults={
        'PROD_CATEGORIA':cat8,
        'PROD_NOMBRE':"BIOGEN BOTOX",
        'CONTENIDO_PZS':"400 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':290.00,
        'PROD_PRECIO_PUB':360.00,
        'PROD_GRAMAJE':400.00
        }
    )
    if created:
        print(f"Producto '{prod165.PROD_NOMBRE}' (CO001) creado.")
    else:
        print(f"Producto '{prod165.PROD_NOMBRE}' (CO001) ya existía. Actualizando gramaje.")
        prod165.PROD_GRAMAJE = 400.00
        prod165.save()
        print(f"Producto '{prod165.PROD_NOMBRE}' (CO001) actualizado con gramaje.")

    prod166, created = Producto.objects.update_or_create(
        ID_PRODUCTO="CO002",
        defaults={
        'PROD_CATEGORIA':cat8,
        'PROD_NOMBRE':"COLAGENO HIDROLIZADO CON PREBIOTICOS CITRUS GREEN",
        'CONTENIDO_PZS':"750 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':550.00,
        'PROD_PRECIO_PUB':650.00,
        'PROD_GRAMAJE':750.00
        }
    )
    if created:
        print(f"Producto '{prod166.PROD_NOMBRE}' (CO002) creado.")
    else:
        print(f"Producto '{prod166.PROD_NOMBRE}' (CO002) ya existía. Actualizando gramaje.")
        prod166.PROD_GRAMAJE = 750.00
        prod166.save()
        print(f"Producto '{prod166.PROD_NOMBRE}' (CO002) actualizado con gramaje.")

    prod167, created = Producto.objects.update_or_create(
        ID_PRODUCTO="CO003",
        defaults={
        'PROD_CATEGORIA':cat8,
        'PROD_NOMBRE':"COLAGENO HIDROLIZADO CON PREBIOTICOS FRUTOS ROJOS",
        'CONTENIDO_PZS':"750 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':550.00,
        'PROD_PRECIO_PUB':650.00,
        'PROD_GRAMAJE':750.00
        }
    )
    if created:
        print(f"Producto '{prod167.PROD_NOMBRE}' (CO003) creado.")
    else:
        print(f"Producto '{prod167.PROD_NOMBRE}' (CO003) ya existía. Actualizando gramaje.")
        prod167.PROD_GRAMAJE = 750.00
        prod167.save()
        print(f"Producto '{prod167.PROD_NOMBRE}' (CO003) actualizado con gramaje.")

    prod168, created = Producto.objects.update_or_create(
        ID_PRODUCTO="CO004",
        defaults={
        'PROD_CATEGORIA':cat8,
        'PROD_NOMBRE':"COLAGENO HIDROLIZADO CON PREBIOTICOS NARANJA ORIENTAL",
        'CONTENIDO_PZS':"750 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':550.00,
        'PROD_PRECIO_PUB':650.00,
        'PROD_GRAMAJE':750.00
        }
    )
    if created:
        print(f"Producto '{prod168.PROD_NOMBRE}' (CO004) creado.")
    else:
        print(f"Producto '{prod168.PROD_NOMBRE}' (CO004) ya existía. Actualizando gramaje.")
        prod168.PROD_GRAMAJE = 750.00
        prod168.save()
        print(f"Producto '{prod168.PROD_NOMBRE}' (CO004) actualizado con gramaje.")

    # FAT BURNERS

    prod169, created = Producto.objects.update_or_create(
        ID_PRODUCTO="NU015",
        defaults={
        'PROD_CATEGORIA':cat9,
        'PROD_NOMBRE':"BERBERINE FAT BURNER",
        'CONTENIDO_PZS':"60 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':370.00,
        'PROD_PRECIO_PUB':460.00,
        }
    )
    if created:
        print(f"Producto '{prod169.PROD_NOMBRE}' (NU015) creado.")
    else:
        print(f"Producto '{prod169.PROD_NOMBRE}' (NU015) ya existía.")
        print(f"Producto '{prod101.PROD_NOMBRE}' (MI014) no se actualizó el gramaje.")

    prod170, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SBELT008",
        defaults={
        'PROD_CATEGORIA':cat9,
        'PROD_NOMBRE':"LIPOSKULTURAL (750 mg)",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':190.00,
        'PROD_PRECIO_PUB':254.00,
        'PROD_GRAMAJE':67.50
        }
    )
    if created:
        print(f"Producto '{prod170.PROD_NOMBRE}' (SBELT008) creado.")
    else:
        print(f"Producto '{prod170.PROD_NOMBRE}' (SBELT008) ya existía. Actualizando gramaje.")
        prod168.PROD_GRAMAJE = 67.50
        prod168.save()
        print(f"Producto '{prod170.PROD_NOMBRE}' (SBELT008) actualizado con gramaje.")
    
    prod171, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SBELT009",
        defaults={
        'PROD_CATEGORIA':cat9,
        'PROD_NOMBRE':"LIPOSKULTURAL (750 mg)",
        'CONTENIDO_PZS':"160 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':344.00,
        'PROD_PRECIO_PUB':460.00,
        'PROD_GRAMAJE':120.00
        }
    )
    if created:
        print(f"Producto '{prod171.PROD_NOMBRE}' (SBELT009) creado.")
    else:
        print(f"Producto '{prod171.PROD_NOMBRE}' (SBELT009) ya existía. Actualizando gramaje.")
        prod171.PROD_GRAMAJE = 120.00
        prod171.save()
        print(f"Producto '{prod171.PROD_NOMBRE}' (SBELT009) actualizado con gramaje.")

    prod172, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SBELT010",
        defaults={
        'PROD_CATEGORIA':cat9,
        'PROD_NOMBRE':"LIPOSKULTURAL",
        'CONTENIDO_PZS':"500 gramos",
        'PROD_DESCRIPCION':"Crema",
        'PROD_PRECIO_MAY':210.00,
        'PROD_PRECIO_PUB':260.00,
        'PROD_GRAMAJE':500.00
        }
    )
    if created:
        print(f"Producto '{prod172.PROD_NOMBRE}' (SBELT010) creado.")
    else:
        print(f"Producto '{prod172.PROD_NOMBRE}' (SBELT010) ya existía. Actualizando gramaje.")
        prod172.PROD_GRAMAJE = 500.00
        prod172.save()
        print(f"Producto '{prod172.PROD_NOMBRE}' (SBELT010) actualizado con gramaje.")

    prod173, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP015",
        defaults={
        'PROD_CATEGORIA':cat9,
        'PROD_NOMBRE':"SBELT LIGHT FRESA",
        'CONTENIDO_PZS':"400 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':238.00,
        'PROD_PRECIO_PUB':280.00,
        'PROD_GRAMAJE':400.00
        }
    )
    if created:
        print(f"Producto '{prod173.PROD_NOMBRE}' (SP016) creado.")
    else:
        print(f"Producto '{prod173.PROD_NOMBRE}' (SP016) ya existía. Actualizando gramaje.")
        prod173.PROD_GRAMAJE = 400.00
        prod173.save()
        print(f"Producto '{prod173.PROD_NOMBRE}' (SP016) actualizado con gramaje.")

    prod174, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP017",
        defaults={
        'PROD_CATEGORIA':cat9,
        'PROD_NOMBRE':"SBELT LIGHT FRESA",
        'CONTENIDO_PZS':"800 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':360.00,
        'PROD_PRECIO_PUB':420.00,
        'PROD_GRAMAJE':800.00
        }
    )
    if created:
        print(f"Producto '{prod174.PROD_NOMBRE}' (SP017) creado.")
    else:
        print(f"Producto '{prod174.PROD_NOMBRE}' (SP017) ya existía. Actualizando gramaje.")
        prod174.PROD_GRAMAJE = 800.00
        prod174.save()
        print(f"Producto '{prod174.PROD_NOMBRE}' (SP017) actualizado con gramaje.")

    prod175, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP018",
        defaults={
        'PROD_CATEGORIA':cat9,
        'PROD_NOMBRE':"SBELT LIGHT VAINILLA",
        'CONTENIDO_PZS':"400 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':238.00,
        'PROD_PRECIO_PUB':280.00,
        'PROD_GRAMAJE':400.00
        }
    )
    if created:
        print(f"Producto '{prod175.PROD_NOMBRE}' (SP018) creado.")
    else:
        print(f"Producto '{prod175.PROD_NOMBRE}' (SP018) ya existía. Actualizando gramaje.")
        prod175.PROD_GRAMAJE = 400.00
        prod175.save()
        print(f"Producto '{prod175.PROD_NOMBRE}' (SP018) actualizado con gramaje.")

    prod176, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP019",
        defaults={
        'PROD_CATEGORIA':cat9,
        'PROD_NOMBRE':"SBELT LIGHT VAINILLA",
        'CONTENIDO_PZS':"800 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':360.00,
        'PROD_PRECIO_PUB':420.00,
        'PROD_GRAMAJE':800.00
        }
    )
    if created:
        print(f"Producto '{prod176.PROD_NOMBRE}' (SP019) creado.")
    else:
        print(f"Producto '{prod176.PROD_NOMBRE}' (SP019) ya existía. Actualizando gramaje.")
        prod176.PROD_GRAMAJE = 800.00
        prod176.save()
        print(f"Producto '{prod176.PROD_NOMBRE}' (SP019) actualizado con gramaje.")

    prod177, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP020",
        defaults={
        'PROD_CATEGORIA':cat9,
        'PROD_NOMBRE':"SBELT LIGHT CHOCOLATE",
        'CONTENIDO_PZS':"400 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':238.00,
        'PROD_PRECIO_PUB':280.00,
        'PROD_GRAMAJE':400.00
        }
    )
    if created:
        print(f"Producto '{prod177.PROD_NOMBRE}' (SP020) creado.")
    else:
        print(f"Producto '{prod177.PROD_NOMBRE}' (SP020) ya existía. Actualizando gramaje.")
        prod177.PROD_GRAMAJE = 400.00
        prod177.save()
        print(f"Producto '{prod177.PROD_NOMBRE}' (SP020) actualizado con gramaje.")

    prod178, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP021",
        defaults={
        'PROD_CATEGORIA':cat9,
        'PROD_NOMBRE':"SBELT LIGHT CHOCOLATE",
        'CONTENIDO_PZS':"800 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':360.00,
        'PROD_PRECIO_PUB':420.00,
        'PROD_GRAMAJE':800.00
        }
    )
    if created:
        print(f"Producto '{prod178.PROD_NOMBRE}' (SP021) creado.")
    else:
        print(f"Producto '{prod178.PROD_NOMBRE}' (SP021) ya existía. Actualizando gramaje.")
        prod178.PROD_GRAMAJE = 800.00
        prod178.save()
        print(f"Producto '{prod178.PROD_NOMBRE}' (SP021) actualizado con gramaje.")

    prod179, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SBELT007",
        defaults={
        'PROD_CATEGORIA':cat9,
        'PROD_NOMBRE':"SUPRA HUNGRY (750 mg)",
        'CONTENIDO_PZS':"90 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':136.00,
        'PROD_PRECIO_PUB':182.00,
        'PROD_GRAMAJE':750.00
        }
    )
    if created:
        print(f"Producto '{prod179.PROD_NOMBRE}' (SBELT007) creado.")
    else:
        print(f"Producto '{prod179.PROD_NOMBRE}' (SBELT007) ya existía. Actualizando gramaje.")
        prod179.PROD_GRAMAJE = 750.00
        prod179.save()
        print(f"Producto '{prod179.PROD_NOMBRE}' (SBELT007) actualizado con gramaje.")

    prod180, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SBELT011",
        defaults={
        'PROD_CATEGORIA':cat9,
        'PROD_NOMBRE':"SUPRA HUNGRY (750 mg)",
        'CONTENIDO_PZS':"160 piezas",
        'PROD_DESCRIPCION':"Cápsulas",
        'PROD_PRECIO_MAY':217.00,
        'PROD_PRECIO_PUB':290.00,
        'PROD_GRAMAJE':750.00
        }
    )
    if created:
        print(f"Producto '{prod180.PROD_NOMBRE}' (SBELT011) creado.")
    else:
        print(f"Producto '{prod180.PROD_NOMBRE}' (SBELT011) ya existía. Actualizando gramaje.")
        prod180.PROD_GRAMAJE = 750.00
        prod180.save()
        print(f"Producto '{prod180.PROD_NOMBRE}' (SBELT011) actualizado con gramaje.")

    prod181, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP028",
        defaults={
        'PROD_CATEGORIA':cat9,
        'PROD_NOMBRE':"THERMOX KETO COFFEE AMERICANO",
        'CONTENIDO_PZS':"300 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':330.00,
        'PROD_PRECIO_PUB':380.00,
        'PROD_GRAMAJE':300.00
        }
    )
    if created:
        print(f"Producto '{prod181.PROD_NOMBRE}' (SP028) creado.")
    else:
        print(f"Producto '{prod181.PROD_NOMBRE}' (SP028) ya existía. Actualizando gramaje.")
        prod181.PROD_GRAMAJE = 300.00
        prod181.save()
        print(f"Producto '{prod181.PROD_NOMBRE}' (SP028) actualizado con gramaje.")

    prod182, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP029",
        defaults={
        'PROD_CATEGORIA':cat9,
        'PROD_NOMBRE':"THERMOX KETO COFFEE AMERICANO",
        'CONTENIDO_PZS':"Sobre de 10 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':25.00,
        'PROD_PRECIO_PUB':30.00,
        'PROD_GRAMAJE':10.00
        }
    )
    if created:
        print(f"Producto '{prod182.PROD_NOMBRE}' (SP029) creado.")
    else:
        print(f"Producto '{prod182.PROD_NOMBRE}' (SP029) ya existía. Actualizando gramaje.")
        prod182.PROD_GRAMAJE = 10.00
        prod182.save()
        print(f"Producto '{prod182.PROD_NOMBRE}' (SP029) actualizado con gramaje.")

    prod183, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP030",
        defaults={
        'PROD_CATEGORIA':cat9,
        'PROD_NOMBRE':"THERMOX KETO COFFEE LATTE",
        'CONTENIDO_PZS':"300 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':390.00,
        'PROD_PRECIO_PUB':460.00,
        'PROD_GRAMAJE':300.00
        }
    )
    if created:
        print(f"Producto '{prod183.PROD_NOMBRE}' (SP030) creado.")
    else:
        print(f"Producto '{prod183.PROD_NOMBRE}' (SP030) ya existía. Actualizando gramaje.")
        prod183.PROD_GRAMAJE = 300.00
        prod183.save()
        print(f"Producto '{prod183.PROD_NOMBRE}' (SP030) actualizado con gramaje.")

    prod184, created = Producto.objects.update_or_create(
        ID_PRODUCTO="SP031",
        defaults={
        'PROD_CATEGORIA':cat9,
        'PROD_NOMBRE':"THERMOX KETO COFFEE LATTE",
        'CONTENIDO_PZS':"Sobre de 10 gramos",
        'PROD_DESCRIPCION':"Polvo",
        'PROD_PRECIO_MAY':25.00,
        'PROD_PRECIO_PUB':30.00,
        'PROD_GRAMAJE':10.00
        }
    )
    if created:
        print(f"Producto '{prod184.PROD_NOMBRE}' (SP031) creado.")
    else:
        print(f"Producto '{prod184.PROD_NOMBRE}' (SP031) ya existía. Actualizando gramaje.")
        prod184.PROD_GRAMAJE = 10.00
        prod184.save()
        print(f"Producto '{prod184.PROD_NOMBRE}' (SP031) actualizado con gramaje.")

    prod185, created = Producto.objects.update_or_create(
        ID_PRODUCTO="CTR001",
        defaults={
        'PROD_CATEGORIA':cat9,
        'PROD_NOMBRE':"THERMO ONE CREMA TERMINA REDUCTORA",
        'CONTENIDO_PZS':"240 gramos",
        'PROD_DESCRIPCION':"Crema",
        'PROD_PRECIO_MAY':320.00,
        'PROD_PRECIO_PUB':400.00,
        'PROD_GRAMAJE':240.00
        }
    )
    if created:
        print(f"Producto '{prod185.PROD_NOMBRE}' (CTR001) creado.")
    else:
        print(f"Producto '{prod185.PROD_NOMBRE}' (CTR001) ya existía. Actualizando gramaje.")
        prod185.PROD_GRAMAJE = 240.00
        prod185.save()
        print(f"Producto '{prod185.PROD_NOMBRE}' (CTR001) actualizado con gramaje.")

    prod186, created = Producto.objects.update_or_create(
        ID_PRODUCTO="CTR002",
        defaults={
        'PROD_CATEGORIA':cat9,
        'PROD_NOMBRE':"THERMO ONE CREMA TERMINA REDUCTORA",
        'CONTENIDO_PZS':"500 gramos",
        'PROD_DESCRIPCION':"Crema",
        'PROD_PRECIO_MAY':510.00,
        'PROD_PRECIO_PUB':600.00,
        'PROD_GRAMAJE':500.00
        }
    )
    if created:
        print(f"Producto '{prod186.PROD_NOMBRE}' (CTR002) creado.")
    else:
        print(f"Producto '{prod186.PROD_NOMBRE}' (CTR002) ya existía. Actualizando gramaje.")
        prod186.PROD_GRAMAJE = 500.00
        prod186.save()
        print(f"Producto '{prod186.PROD_NOMBRE}' (CTR002) actualizado con gramaje.")


if __name__ == "__main__":
    inserciones()
    print(Producto.objects.all())

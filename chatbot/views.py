from django.shortcuts import render
import google.generativeai as genai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .knowledge_base import STORE_INFO, PRODUCT_CATEGORIES, COMMON_QUESTIONS, PRODUCT_BENEFITS, RECOMMENDATIONS
from products.models import Producto, Categoria

GEMINI_API_KEY = "AIzaSyBIRWLakhEh64qWXdw6p7DCLf8JDuI-ALc"  # API Key proporcionada

genai.configure(api_key=GEMINI_API_KEY)

def get_store_context():
    """Genera el contexto de la tienda para el chatbot"""
    context = f"""
    Eres un asistente virtual especializado de {STORE_INFO['name']}, una {STORE_INFO['type']}.

    INFORMACIÓN DE LA TIENDA:
    - Nombre: {STORE_INFO['name']}
    - Especialización: {STORE_INFO['specialization']}
    - Descripción: {STORE_INFO['description']}

    CATEGORÍAS DE PRODUCTOS QUE VENDEMOS:
    """

    for category, info in PRODUCT_CATEGORIES.items():
        context += f"\n{category.upper()}:\n"
        context += f"- Descripción: {info['description']}\n"
        context += "- Productos disponibles:\n"
        for product in info['products']:
            context += f"  • {product}\n"

    context += f"""

    PREGUNTAS FRECUENTES:
    - ¿Qué vendemos?: {COMMON_QUESTIONS['que_vendemos']}
    - Horarios: {COMMON_QUESTIONS['horarios']}
    - Envíos: {COMMON_QUESTIONS['envios']}
    - Calidad: {COMMON_QUESTIONS['calidad']}
    - Asesoramiento: {COMMON_QUESTIONS['asesoramiento']}

    INSTRUCCIONES IMPORTANTES:
    1. Siempre responde como un experto en suplementos nutricionales de BioCommerce
    2. Proporciona información útil y precisa sobre nuestros productos
    3. Si te preguntan sobre productos que no tenemos, sugiere alternativas similares de nuestro catálogo
    4. Mantén un tono amigable, profesional y orientado a ayudar al cliente
    5. Si no tienes información específica sobre algo, admítelo y ofrece contactar con nuestro equipo
    6. Siempre prioriza la salud y seguridad del cliente
    7. Responde en español de manera clara y comprensible
    """

    return context

def get_product_recommendations(user_message):
    """Analiza el mensaje del usuario y sugiere productos relevantes"""
    message_lower = user_message.lower()

    # Palabras clave para diferentes categorías
    keywords = {
        'principiantes': ['principiante', 'empezar', 'comenzar', 'nuevo', 'básico'],
        'deportistas': ['deportista', 'gym', 'gimnasio', 'entrenar', 'músculo', 'fuerza', 'rendimiento'],
        'salud_general': ['salud', 'bienestar', 'general', 'diario', 'mantenimiento'],
        'mujeres': ['mujer', 'femenino', 'embarazo', 'menopausia']
    }

    for category, words in keywords.items():
        if any(word in message_lower for word in words):
            return RECOMMENDATIONS.get(category, [])

    return []

def get_real_products_info():
    """Obtiene información de productos reales de la base de datos"""
    try:
        productos = Producto.objects.select_related('categoria').all()[:20]  # Limitar a 20 productos
        productos_info = []

        for producto in productos:
            info = {
                'nombre': producto.nombre,
                'categoria': producto.categoria.nombre if producto.categoria else 'Sin categoría',
                'precio': float(producto.precio) if producto.precio else 0,
                'descripcion': producto.descripcion[:100] + '...' if len(producto.descripcion) > 100 else producto.descripcion
            }
            productos_info.append(info)

        return productos_info
    except Exception as e:
        return []

def search_products_by_keyword(keyword):
    """Busca productos por palabra clave en nombre o descripción"""
    try:
        productos = Producto.objects.filter(
            nombre__icontains=keyword
        ).select_related('categoria')[:5]

        if not productos:
            productos = Producto.objects.filter(
                descripcion__icontains=keyword
            ).select_related('categoria')[:5]

        productos_encontrados = []
        for producto in productos:
            info = f"• {producto.nombre} - ${producto.precio} ({producto.categoria.nombre if producto.categoria else 'Sin categoría'})"
            productos_encontrados.append(info)

        return productos_encontrados
    except Exception as e:
        return []

@csrf_exempt
def chatbot_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")
        # Obtener contexto de la tienda
        store_context = get_store_context()

        # Obtener recomendaciones si es relevante
        recommendations = get_product_recommendations(user_message)

        # Buscar productos específicos si el usuario menciona algún término
        search_terms = ['producto', 'precio', 'comprar', 'vender', 'disponible', 'stock']
        products_info = []

        if any(term in user_message.lower() for term in search_terms):
            # Extraer palabras clave del mensaje para buscar productos
            words = user_message.lower().split()
            for word in words:
                if len(word) > 3:  # Solo buscar palabras de más de 3 caracteres
                    found_products = search_products_by_keyword(word)
                    if found_products:
                        products_info.extend(found_products)
                        break  # Solo usar la primera palabra clave que encuentre productos

        # Construir el prompt completo
        full_prompt = f"{store_context}\n\nPREGUNTA DEL CLIENTE: {user_message}"

        if recommendations:
            full_prompt += f"\n\nRECOMENDACIONES SUGERIDAS: {', '.join(recommendations)}"

        if products_info:
            full_prompt += f"\n\nPRODUCTOS ENCONTRADOS EN NUESTRA TIENDA:\n" + "\n".join(products_info[:5])

        try:
            model = genai.GenerativeModel("gemini-2.0-flash")
            response = model.generate_content(full_prompt)
            bot_reply = response.text if hasattr(response, "text") else "Lo siento, no pude procesar tu consulta en este momento."
        except Exception as e:
            # Log del error para depuración
            print(f"Error en chatbot: {str(e)}")
            print(f"Tipo de error: {type(e).__name__}")
            bot_reply = "Disculpa, estoy experimentando dificultades técnicas. Por favor, intenta nuevamente en unos momentos."
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(user_message)
        bot_reply = response.text if hasattr(response, "text") else "Lo siento, no entendí tu pregunta."

        return JsonResponse({"reply": bot_reply})
    return JsonResponse({"error": "Método no permitido"}, status=405)

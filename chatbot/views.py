from django.shortcuts import render
import google.generativeai as genai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging
import os
import requests
from django.conf import settings
from .knowledge_base import STORE_INFO, PRODUCT_CATEGORIES, COMMON_QUESTIONS, PRODUCT_BENEFITS, RECOMMENDATIONS
from products.models import Producto, Categoria

logger = logging.getLogger(__name__)

# Toma la API key desde settings o variable de entorno; evita hardcode.
GEMINI_API_KEY = getattr(settings, 'GEMINI_API_KEY', os.environ.get('GEMINI_API_KEY'))
if GEMINI_API_KEY:
    try:
        # Asegura que la librería detecte la API key vía entorno
        os.environ.setdefault('GOOGLE_API_KEY', GEMINI_API_KEY)
        genai.configure(api_key=GEMINI_API_KEY)
    except Exception:
        logger.exception("No se pudo configurar Gemini con la API key")

# Modelos candidatos (fallback ante modelos no disponibles para la cuenta o versión)
MODEL_CANDIDATES = [
    getattr(settings, 'GEMINI_MODEL', 'gemini-1.5-flash-latest'),
    'gemini-1.5-pro-latest',
    'gemini-1.5-flash',
    'gemini-1.0-pro',
    'gemini-pro',
]

# Preferencias de modelos gratuitos o de menor costo
FREE_MODEL_PREFERENCES = [
    # Primero los modelos gratuitos legacy
    'chat-bison-001',
    'text-bison-001',
    # Luego los flash (más económicos)
    'gemini-1.5-flash-latest',
    'gemini-1.5-flash',
    'gemini-1.5-flash-8b',
    # Finalmente pro/legacy
    'gemini-1.0-pro',
    'gemini-pro',
]

def _extract_text_from_candidates(data: dict) -> str:
    """Intenta extraer texto de diferentes esquemas de respuesta."""
    candidates = data.get("candidates", [])
    if candidates:
        # Gemini y chat-bison devuelven content.parts[].text
        content = candidates[0].get("content", {})
        parts = content.get("parts", [])
        for part in parts:
            if isinstance(part, dict) and part.get("text"):
                return part.get("text")
        # text-bison devuelve output directo
        if candidates[0].get("output"):
            return candidates[0].get("output")
    return None

def _generate_with_rest(model_name: str, prompt: str, version: str = "v1") -> str:
    """Fallback REST para generar contenido.
    Por defecto usa v1 (Gemini). Devuelve texto o None si falla.
    """
    if not GEMINI_API_KEY:
        return None
    try:
        url = f"https://generativelanguage.googleapis.com/{version}/models/{model_name}:generateContent"
        params = {"key": GEMINI_API_KEY}
        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": prompt}],
                }
            ]
        }
        resp = requests.post(url, params=params, json=payload, timeout=12)
        resp.raise_for_status()
        data = resp.json()
        return _extract_text_from_candidates(data)
    except Exception:
        logger.exception(f"Fallback REST ({version}): error con modelo '{model_name}'")
        return None

def _generate_with_rest_bison(model_name: str, prompt: str) -> str:
    """Llamadas REST para modelos bison (v1beta2): text-bison / chat-bison."""
    if not GEMINI_API_KEY:
        return None
    try:
        # text-bison usa generateText, chat-bison usa generateMessage
        if model_name == 'text-bison-001':
            url = f"https://generativelanguage.googleapis.com/v1beta2/models/{model_name}:generateText"
            params = {"key": GEMINI_API_KEY}
            payload = {"prompt": {"text": prompt}}
        elif model_name == 'chat-bison-001':
            url = f"https://generativelanguage.googleapis.com/v1beta2/models/{model_name}:generateMessage"
            params = {"key": GEMINI_API_KEY}
            payload = {"prompt": {"messages": [{"author": "user", "content": prompt}]}}
        else:
            return None
        resp = requests.post(url, params=params, json=payload, timeout=12)
        resp.raise_for_status()
        data = resp.json()
        # text-bison: candidates[0].output; chat-bison: candidates[0].content.parts[0].text
        return _extract_text_from_candidates(data)
    except Exception:
        logger.exception(f"Fallback REST (v1beta2): error con modelo '{model_name}'")
        return None

def list_available_models(version: str = "v1") -> list:
    """Obtiene lista de modelos accesibles para la API key en la versión dada."""
    if not GEMINI_API_KEY:
        return []
    try:
        url = f"https://generativelanguage.googleapis.com/{version}/models"
        params = {"key": GEMINI_API_KEY}
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        models = data.get("models", [])
        names = []
        for m in models:
            name = m.get("name") or m.get("id") or ""
            if name:
                names.append(name.split("/")[-1])
        return names
    except Exception:
        logger.exception(f"ListModels ({version}) falló")
        return []

def compose_rule_based_reply(user_message: str, recommendations: list, products_info: list) -> str:
    """Genera una respuesta útil sin LLM usando reglas y catálogo."""
    lines = []
    lines.append("Gracias por tu consulta. Te comparto una recomendación basada en nuestro catálogo:")
    if recommendations:
        lines.append("\nSugerencias según tu objetivo:")
        for rec in recommendations[:5]:
            lines.append(f"• {rec}")
    if products_info:
        lines.append("\nProductos disponibles que podrían interesarte:")
        for p in products_info[:5]:
            lines.append(p)
    lines.append("\nSi quieres, dime tu objetivo (masa muscular, definición, energía) y presupuesto, y te doy una recomendación más precisa.")
    lines.append("Para dudas de envío, horarios o stock, también te ayudo.")
    return "\n".join(lines)

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
        # Validación de JSON y del mensaje
        try:
            body = request.body.decode('utf-8') if isinstance(request.body, (bytes, bytearray)) else request.body
            data = json.loads(body or '{}')
        except Exception:
            logger.exception("JSON inválido en petición del chatbot")
            return JsonResponse({"error": "JSON inválido"}, status=400)

        user_message = str(data.get("message", "")).strip()
        if not user_message:
            return JsonResponse({"error": "El campo 'message' es requerido"}, status=400)

        # Obtener contexto de la tienda y construir el prompt
        store_context = get_store_context()
        full_prompt = f"{store_context}\n\nPREGUNTA DEL CLIENTE: {user_message}"

        bot_reply = None
        model_name = getattr(settings, 'GEMINI_MODEL', 'gemini-2.5-flash')

        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(full_prompt)
            bot_reply = getattr(response, "text", None)
            if bot_reply:
                logger.info(f"Respuesta obtenida con modelo '{model_name}'")
            else:
                # Si el modelo no devuelve texto, usa un mensaje genérico
                logger.warning(f"El modelo '{model_name}' no devolvió contenido de texto.")
                bot_reply = "No se pudo obtener una respuesta del modelo en este momento."

        except Exception:
            logger.exception(f"Error generando contenido con modelo '{model_name}'")
            bot_reply = "Lo siento, estoy teniendo dificultades técnicas para procesar tu solicitud."

        return JsonResponse({"reply": bot_reply})

    return JsonResponse({"error": "Método no permitido"}, status=405)

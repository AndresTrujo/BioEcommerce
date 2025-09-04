from django.shortcuts import render

import google.generativeai as genai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

GEMINI_API_KEY = "AIzaSyBIRWLakhEh64qWXdw6p7DCLf8JDuI-ALc"  # API Key proporcionada

genai.configure(api_key=GEMINI_API_KEY)

@csrf_exempt
def chatbot_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_message)
        bot_reply = response.text if hasattr(response, "text") else "Lo siento, no entendí tu pregunta."

        return JsonResponse({"reply": bot_reply})
    return JsonResponse({"error": "Método no permitido"}, status=405)

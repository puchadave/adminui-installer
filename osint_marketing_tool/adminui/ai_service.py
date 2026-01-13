from flask import Blueprint, request, jsonify
from utils.openai_client import OpenAIClient
from utils.gemini_client import GeminiClient
from utils.ollama_client import OllamaClient

ai_service_bp = Blueprint('ai_service', __name__)

# Initialize AI clients
openai_client = OpenAIClient()
gemini_client = GeminiClient()
ollama_client = OllamaClient()

@ai_service_bp.route('/api/ai/openai', methods=['POST'])
def openai_service():
    data = request.json
    response = openai_client.send_request(data)
    return jsonify(response)

@ai_service_bp.route('/api/ai/gemini', methods=['POST'])
def gemini_service():
    data = request.json
    response = gemini_client.send_request(data)
    return jsonify(response)

@ai_service_bp.route('/api/ai/ollama', methods=['POST'])
def ollama_service():
    data = request.json
    response = ollama_client.send_request(data)
    return jsonify(response)
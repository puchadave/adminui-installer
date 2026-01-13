from flask import Blueprint, render_template, request, jsonify
from utils.openai_client import OpenAIClient
from utils.gemini_client import GeminiClient
from utils.ollama_client import OllamaClient

admin_ai_bp = Blueprint('admin_ai', __name__)

# Initialize AI clients
openai_client = OpenAIClient()
gemini_client = GeminiClient()
ollama_client = OllamaClient()

@admin_ai_bp.route('/admin/ai', methods=['GET'])
def admin_ai():
    return render_template('admin_ai.html')

@admin_ai_bp.route('/api/ai/chat', methods=['POST'])
def ai_chat():
    data = request.json
    prompt = data.get('prompt')
    model = data.get('model', 'openai')  # Default to OpenAI

    if model == 'openai':
        response = openai_client.chat(prompt)
    elif model == 'gemini':
        response = gemini_client.chat(prompt)
    elif model == 'ollama':
        response = ollama_client.chat(prompt)
    else:
        return jsonify({'error': 'Invalid model specified'}), 400

    return jsonify({'response': response})
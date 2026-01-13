from flask import Blueprint, jsonify, request
from utils.openai_client import OpenAIClient
from utils.gemini_client import GeminiClient
from utils.ollama_client import OllamaClient

backup_ai_bp = Blueprint('backup_ai', __name__)

@backup_ai_bp.route('/api/ai_backup', methods=['POST'])
def ai_backup():
    data = request.json
    tenant_id = data.get('tenant_id')
    
    if not tenant_id:
        return jsonify({'error': 'Tenant ID is required'}), 400

    # Initialize AI clients
    openai_client = OpenAIClient()
    gemini_client = GeminiClient()
    ollama_client = OllamaClient()

    # Perform AI-driven backup logic here
    # Example: Use AI clients to gather data and perform backup
    try:
        # Example interaction with AI clients
        openai_response = openai_client.perform_backup(tenant_id)
        gemini_response = gemini_client.perform_backup(tenant_id)
        ollama_response = ollama_client.perform_backup(tenant_id)

        return jsonify({
            'status': 'success',
            'openai_response': openai_response,
            'gemini_response': gemini_response,
            'ollama_response': ollama_response
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Register the blueprint in app.py
# from backup_ai import backup_ai_bp
# app.register_blueprint(backup_ai_bp)
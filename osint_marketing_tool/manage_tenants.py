from flask import Blueprint, request, jsonify
from tenants import TenantManager
from utils.openai_client import OpenAIClient
from utils.gemini_client import GeminiClient
from utils.ollama_client import OllamaClient

manage_tenants_bp = Blueprint('manage_tenants', __name__)

tenant_manager = TenantManager()
openai_client = OpenAIClient()
gemini_client = GeminiClient()
ollama_client = OllamaClient()

@manage_tenants_bp.route('/tenants', methods=['GET'])
def list_tenants():
    tenants = tenant_manager.list_tenants()
    return jsonify(tenants)

@manage_tenants_bp.route('/tenants/<tenant_id>', methods=['GET'])
def get_tenant(tenant_id):
    tenant = tenant_manager.get_tenant(tenant_id)
    if tenant:
        return jsonify(tenant)
    return jsonify({'error': 'Tenant not found'}), 404

@manage_tenants_bp.route('/tenants', methods=['POST'])
def create_tenant():
    data = request.json
    tenant_id = tenant_manager.create_tenant(data)
    return jsonify({'tenant_id': tenant_id}), 201

@manage_tenants_bp.route('/tenants/<tenant_id>', methods=['PUT'])
def update_tenant(tenant_id):
    data = request.json
    success = tenant_manager.update_tenant(tenant_id, data)
    if success:
        return jsonify({'message': 'Tenant updated successfully'})
    return jsonify({'error': 'Tenant not found or update failed'}), 404

@manage_tenants_bp.route('/tenants/<tenant_id>', methods=['DELETE'])
def delete_tenant(tenant_id):
    success = tenant_manager.delete_tenant(tenant_id)
    if success:
        return jsonify({'message': 'Tenant deleted successfully'})
    return jsonify({'error': 'Tenant not found'}), 404

@manage_tenants_bp.route('/ai/openai', methods=['POST'])
def call_openai():
    data = request.json
    response = openai_client.send_request(data)
    return jsonify(response)

@manage_tenants_bp.route('/ai/gemini', methods=['POST'])
def call_gemini():
    data = request.json
    response = gemini_client.send_request(data)
    return jsonify(response)

@manage_tenants_bp.route('/ai/ollama', methods=['POST'])
def call_ollama():
    data = request.json
    response = ollama_client.send_request(data)
    return jsonify(response)
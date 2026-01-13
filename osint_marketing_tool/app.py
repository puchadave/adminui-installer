from users import user_bp
from tenants import tenant_bp
from adminui import admin_ui_bp
from utils.openai_client import OpenAIClient
from utils.gemini_client import GeminiClient
from utils.ollama_client import OllamaClient

app = Flask(__name__)

# Register blueprints for various modules
app.register_blueprint(user_bp)
app.register_blueprint(tenant_bp)
app.register_blueprint(admin_ui_bp)

# Configuration for multi-tenancy
app.config['TENANT_STORAGE'] = 'storage/tenants/'

# Initialize AI clients
openai_client = OpenAIClient()
gemini_client = GeminiClient()
ollama_client = OllamaClient()

@app.route('/api/ai_chat', methods=['POST'])
def ai_chat():
    # Logic to handle AI chat requests
    pass

if __name__ == '__main__':
    app.run(debug=True)

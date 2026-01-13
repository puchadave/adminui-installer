from flask import Blueprint

admin_ui_bp = Blueprint('admin_ui', __name__, template_folder='templates')

from . import views, ai_service  # Import views and AI service to register routes and functionalities
from flask import Blueprint, jsonify, request
from services import ia_service

# É esta linha que define o chat_bp que o app.py procura
chat_bp = Blueprint("chat", __name__, url_prefix="/api/chat")

#!/usr/bin/env python3
"""
Dashboard Looker Studio con autenticación y restricción de Safari iOS/macOS
DINTEMAR - Marina de Guerra del Perú
"""

import os
import json
import bcrypt
from datetime import timedelta
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from functools import wraps

app = Flask(__name__)

# Configuración
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'cambia-esto-en-produccion-clave-secreta-super-segura-2025')
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=8)
USERS_FILE = "users.json"


# =============================================================================
# Funciones de Utilidad
# =============================================================================

def load_users():
    """Carga el archivo de usuarios."""
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {"users": []}


def verify_user(username, password):
    """Verifica las credenciales de un usuario."""
    users_data = load_users()

    for user in users_data['users']:
        if user['username'] == username:
            stored_hash = user['password_hash']
            if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
                return True
    return False


def is_safari_ios_macos(user_agent):
    """
    Verifica si el navegador es Safari en iOS o macOS.

    Returns:
        bool: True si es Safari en iOS/macOS, False en caso contrario
    """
    ua = user_agent.lower()

    # Safari en iOS (iPhone o iPad)
    if 'iphone' in ua or 'ipad' in ua:
        return 'safari' in ua

    # Safari en macOS
    # Nota: Chrome también contiene "Safari" en su User-Agent,
    # así que debemos excluir Chrome y Edge
    if 'macintosh' in ua or 'mac os x' in ua:
        is_safari = 'safari' in ua
        # Excluir Chrome (contiene tanto "Chrome" como "Safari")
        is_not_chrome = 'chrome' not in ua
        # Excluir Edge (contiene "Edg")
        is_not_edge = 'edg' not in ua
        # Excluir Firefox
        is_not_firefox = 'firefox' not in ua

        return is_safari and is_not_chrome and is_not_edge and is_not_firefox

    return False


def login_required(f):
    """Decorator para proteger rutas que requieren autenticación."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


# =============================================================================
# Middleware: Verificación de User Agent
# =============================================================================

@app.before_request
def check_safari_restrictions():
    """
    Verifica que el navegador sea Safari en iOS/macOS antes de procesar cualquier request.
    Excluye las rutas estáticas y la página de bloqueo.
    """
    # Rutas que no requieren verificación de Safari
    excluded_routes = ['static', 'blocked']

    if request.endpoint in excluded_routes:
        return None

    # Obtener User-Agent
    user_agent = request.headers.get('User-Agent', '')

    # Verificar si es Safari en iOS/macOS
    if not is_safari_ios_macos(user_agent):
        # Si no es Safari permitido, mostrar página de bloqueo
        return render_template('blocked.html', user_agent=user_agent), 403

    return None


# =============================================================================
# Rutas de la Aplicación
# =============================================================================

@app.route('/')
def index():
    """Redirige al login o al dashboard según el estado de autenticación."""
    if session.get('logged_in'):
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Maneja el formulario de login.
    GET: Muestra el formulario
    POST: Procesa las credenciales
    """
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        if not username or not password:
            return render_template('login.html', error='Por favor ingrese usuario y contraseña')

        if verify_user(username, password):
            session['logged_in'] = True
            session['username'] = username
            session.permanent = True

            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Credenciales inválidas')

    return render_template('login.html')


@app.route('/dashboard')
@login_required
def dashboard():
    """
    Muestra el dashboard con el iframe de Looker Studio.
    Requiere autenticación.
    """
    return render_template('dashboard.html', username=session.get('username'))


@app.route('/logout')
def logout():
    """Cierra la sesión del usuario."""
    session.clear()
    return redirect(url_for('login'))


@app.route('/check-browser')
def check_browser():
    """
    Endpoint para verificar el navegador desde JavaScript.
    Útil para mostrar mensajes informativos.
    """
    user_agent = request.headers.get('User-Agent', '')
    is_allowed = is_safari_ios_macos(user_agent)

    return jsonify({
        'is_safari_allowed': is_allowed,
        'user_agent': user_agent
    })


# =============================================================================
# Manejo de Errores
# =============================================================================

@app.errorhandler(403)
def forbidden(e):
    """Maneja errores 403 Forbidden."""
    user_agent = request.headers.get('User-Agent', '')
    return render_template('blocked.html', user_agent=user_agent), 403


@app.errorhandler(404)
def not_found(e):
    """Maneja errores 404 Not Found."""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    """Maneja errores 500 Internal Server Error."""
    return render_template('500.html'), 500


# =============================================================================
# Inicialización
# =============================================================================

if __name__ == '__main__':
    # Verificar que existe el archivo de usuarios
    if not os.path.exists(USERS_FILE):
        print("=" * 60)
        print("  ADVERTENCIA: No existe el archivo users.json")
        print("=" * 60)
        print("\nPor favor, ejecute el siguiente comando para crear usuarios:")
        print("  python create_user.py")
        print("\nO cree un usuario con:")
        print("  python create_user.py create admin tu_contraseña")
        print("\n")

    # Verificar si estamos en modo producción
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'

    print("\n" + "=" * 60)
    print("  Dashboard Looker Studio - DINTEMAR")
    print("  Marina de Guerra del Perú")
    print("=" * 60)
    print(f"\nModo: {'DEBUG' if debug_mode else 'PRODUCCIÓN'}")
    print(f"Restricción: Safari iOS/macOS solamente")
    print(f"\nIniciando servidor en http://localhost:5000")
    print("=" * 60 + "\n")

    # Iniciar aplicación
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=debug_mode
    )

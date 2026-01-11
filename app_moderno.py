#!/usr/bin/env python3
"""
Data Analytics Dashboard - Modern Flask App
Sin autenticación - Acceso libre
"""

import os
from flask import Flask, render_template, request
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

# IMPORTANTÍSIMO: Configurar para detrás de proxy (nginx)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

# Configuración de producción
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'data-analytics-dashboard-2025-secure-key')
app.config['SESSION_COOKIE_SECURE'] = True  # Solo enviar cookies sobre HTTPS
app.config['SESSION_COOKIE_HTTPONLY'] = True  # No accesible vía JavaScript
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # Protección CSRF


# =============================================================================
# Funciones de Utilidad
# =============================================================================

def is_allowed_browser(user_agent):
    """
    Verifica si el navegador está permitido según el dispositivo:
    - Mobile (iOS): Solo Safari
    - Desktop: Safari o Firefox

    Returns:
        bool: True si el navegador es permitido, False en caso contrario
    """
    ua = user_agent.lower()

    # Mobile (iOS): Solo Safari
    if 'iphone' in ua or 'ipad' in ua:
        return 'safari' in ua and 'chrome' not in ua and 'edg' not in ua and 'firefox' not in ua

    # Desktop: Safari o Firefox permitidos
    # Detectar si es desktop (no mobile)
    is_mobile = 'iphone' in ua or 'ipad' in ua or 'android' in ua or 'mobile' in ua

    if not is_mobile:
        # Permitir Firefox
        if 'firefox' in ua:
            return True

        # Permitir Safari (excluyendo Chrome y Edge)
        if 'safari' in ua and 'chrome' not in ua and 'edg' not in ua:
            return True

    # Bloquear todos los demás navegadores
    return False


# =============================================================================
# Middleware: Verificación de User Agent
# =============================================================================

@app.before_request
def check_browser_restrictions():
    """
    Verifica que el navegador sea permitido antes de procesar cualquier request.
    Excluye las rutas estáticas y la página de bloqueo.
    """
    # Rutas que no requieren verificación de navegador
    excluded_routes = ['static', 'blocked']

    if request.endpoint in excluded_routes:
        return None

    # Obtener User-Agent
    user_agent = request.headers.get('User-Agent', '')

    # Verificar si el navegador está permitido
    if not is_allowed_browser(user_agent):
        # Si no es un navegador permitido, mostrar página de bloqueo
        return render_template('blocked.html', user_agent=user_agent), 403

    return None


# =============================================================================
# Rutas de la Aplicación
# =============================================================================

@app.route('/')
def index():
    """
    Página principal - Redirige al dashboard.
    """
    return render_template('dashboard_moderno.html')


@app.route('/dashboard')
def dashboard():
    """
    Muestra el dashboard con el iframe de Power BI.
    No requiere autenticación.
    """
    return render_template('dashboard_moderno.html')


@app.route('/dossiers')
def dossiers():
    """
    Muestra la sección de dossiers.
    No requiere autenticación.
    """
    return render_template('dossiers.html')


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
    return render_template('404_moderno.html'), 404


@app.errorhandler(500)
def internal_error(e):
    """Maneja errores 500 Internal Server Error."""
    return render_template('500_moderno.html'), 500


# =============================================================================
# Inicialización
# =============================================================================

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("  Data Analytics Dashboard")
    print("  Versión Moderna - Sin Login")
    print("=" * 60)
    print("\nModo: PRODUCCIÓN")
    print("Restricción: Safari iOS/macOS y Firefox Desktop")
    print("\nIniciando servidor en http://127.0.0.1:5001")
    print("=" * 60 + "\n")

    # Iniciar aplicación
    app.run(
        host='127.0.0.1',
        port=5001,
        debug=False
    )

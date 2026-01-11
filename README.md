# Dashboard Looker Studio - DINTEMAR

Sistema de acceso restringido para dashboard de Looker Studio con autenticación y restricción de navegador.

**Desarrollado para:** DINTEMAR - Marina de Guerra del Perú

---

## Características

- 🔐 **Autenticación segura** mediante Flask Sessions con contraseñas hasheadas (bcrypt)
- 🍎 **Restricción de navegador** - Solo permite acceso desde Safari en iOS/macOS
- 🎨 **Diseño naval institucional** - Estética consistente con DINTEMAR-OSINT
- 📊 **Dashboard embebido** - Iframe de Looker Studio integrado
- ⚡ **Sesiones persistentes** - 8 horas de duración por defecto

---

## Requisitos del Sistema

- **Python:** 3.8 o superior
- **Navegador:** Safari en iOS (iPhone/iPad) o macOS
- **Sistema Operativo:** iOS, macOS, Linux o Windows (para el servidor)

---

## Instalación

### Paso 1: Crear entorno virtual

```bash
cd /home/leinsosint/Escritorio/dashboard-looker
python3 -m venv venv
source venv/bin/activate  # En Linux/macOS
# o
venv\Scripts\activate  # En Windows
```

### Paso 2: Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 3: Crear usuario administrador

**Opción A: Modo interactivo**

```bash
python create_user.py
```

Luego seleccionar "1. Crear nuevo usuario" y seguir las instrucciones.

**Opción B: Línea de comandos**

```bash
python create_user.py create admin tu_contraseña_segura
```

### Paso 4: Iniciar el servidor

**Modo desarrollo (con debug):**

```bash
export FLASK_DEBUG=true
python app.py
```

**Modo producción:**

```bash
python app.py
```

El servidor estará disponible en: `http://localhost:5000`

---

## Uso

### Acceder al Dashboard

1. Abrir Safari en iOS o macOS
2. Navegar a: `http://localhost:5000` (o la IP del servidor)
3. Ingresar credenciales de usuario
4. El dashboard de Looker Studio se cargará automáticamente

### Cerrar Sesión

Hacer clic en el botón "Cerrar Sesión" en la parte superior del dashboard.

---

## Gestión de Usuarios

### Listar usuarios existentes

```bash
python create_user.py list
```

### Crear nuevo usuario

```bash
python create_user.py
# Seleccionar opción 1
```

### Ver usuarios desde línea de comandos

```bash
python create_user.py create <usuario> <contraseña>
```

---

## Configuración Avanzada

### Cambiar puerto del servidor

Editar `app.py` (línea 275):

```python
app.run(
    host='0.0.0.0',
    port=8000,  # Cambiar puerto aquí
    debug=debug_mode
)
```

### Cambiar duración de la sesión

Editar `app.py` (línea 15):

```python
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=12)  # 12 horas
```

### Configurar SECRET_KEY para producción

**Importante:** Cambiar el SECRET_KEY por defecto antes de usar en producción.

**Opción 1: Variable de entorno**

```bash
export SECRET_KEY='tu-clave-secreta-super-larga-y-aleatoria'
python app.py
```

**Opción 2: Editar app.py**

Buscar la línea 14 y cambiar:

```python
app.config['SECRET_KEY'] = 'tu-clave-secreta-super-larga-y-aleatoria-aqui'
```

**Generar clave segura:**

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

---

## Estructura del Proyecto

```
dashboard-looker/
├── app.py                    # Aplicación Flask principal
├── users.json                # Base de datos de usuarios (hasheados)
├── create_user.py            # Script para gestionar usuarios
├── requirements.txt          # Dependencias Python
├── README.md                 # Este archivo
├── templates/
│   ├── login.html           # Página de login
│   ├── dashboard.html       # Dashboard con iframe
│   ├── blocked.html         # Página de navegador no soportado
│   ├── 404.html             # Página de error 404
│   └── 500.html             # Página de error 500
└── static/
    └── css/
        └── styles.css       # Estilos navales
```

---

## Seguridad

### Características de seguridad implementadas

- ✅ Contraseñas hasheadas con bcrypt (salt automático)
- ✅ Archivo `users.json` con permisos restrictivos (600)
- ✅ Sesiones con COOKIE_HTTPONLY y COOKIE_SECURE
- ✅ Protección contra XSS (Jinja2 sanitiza por defecto)
- ✅ Restricción de User Agent para Safari only
- ✅ Timeout de sesión configurable

### Recomendaciones de seguridad

1. **Usar HTTPS en producción** - Configurar SSL/TLS con nginx o Apache
2. **Cambiar SECRET_KEY** - Usar una clave aleatoria larga
3. **Firewall** - Restringir acceso por IP si es necesario
4. **Backups** - Hacer backup regular de `users.json`
5. **Logs** - Monitorear logs de acceso en producción

---

## Troubleshooting

### Error: "No existe el archivo users.json"

**Solución:** Crear un usuario con el script `create_user.py`

```bash
python create_user.py create admin tu_password
```

### El iframe no carga

**Verificaciones:**

1. Conexión a internet activa
2. El URL de Looker Studio es correcto en `dashboard.html`
3. No hay bloqueadores de publicidad en Safari
4. Safari permite iframes de terceros

### Acceso denegado desde Safari

**Verificar User Agent:**

```javascript
// En consola del navegador
console.log(navigator.userAgent);
```

Debe contener:
- iOS: `iPhone` o `iPad` + `Safari`
- macOS: `Macintosh` + `Safari` (pero NO `Chrome`)

### Error de permisos en users.json

**Solución:**

```bash
chmod 600 users.json
```

---

## Navegadores Soportados

| Navegador | Plataforma | Versión | Estado |
|-----------|-----------|---------|--------|
| Safari | iOS (iPhone/iPad) | 12+ | ✅ Soportado |
| Safari | macOS | 12+ | ✅ Soportado |
| Chrome | Cualquiera | - | ❌ Bloqueado |
| Firefox | Cualquiera | - | ❌ Bloqueado |
| Edge | Cualquiera | - | ❌ Bloqueado |

---

## Personalización

### Cambiar el iframe de Looker Studio

Editar `templates/dashboard.html` (línea 105):

```html
<iframe
    src="https://lookerstudio.google.com/embed/reporting/TU_NUEVO_REPORT_ID/page/PAGE_ID"
    ...
</iframe>
```

### Modificar estilos visuales

Editar `static/css/styles.css` para cambiar:
- Colores navales (variables CSS `:root`)
- Tipografías
- Efectos visuales

### Agregar más rutas

Editar `app.py` y agregar nuevos decoradores `@app.route()`:

```python
@app.route('/nueva-ruta')
@login_required
def nueva_ruta():
    return render_template('nuevo_template.html')
```

---

## Deploy en Producción

### Usar Gunicorn (recomendado)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Configurar nginx como reverse proxy

```nginx
server {
    listen 80;
    server_name dashboard.dintemar.mil.pe;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static {
        alias /path/to/dashboard-looker/static;
    }
}
```

---

## Soporte

Para problemas o consultas, contactar al equipo de desarrollo de DINTEMAR.

---

## Licencia

Uso exclusivo para la Marina de Guerra del Perú - DINTEMAR

© 2025 DINTEMAR - Todos los derechos reservados

---

**Versión:** 1.0.0
**Última actualización:** Enero 2025

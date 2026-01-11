# Dashboard Looker Studio - INICIO RÁPIDO

## Usuario Creado Exitosamente

**Usuario:** admin
**Contraseña:** admin123

## Cómo Iniciar el Servidor

```bash
cd /home/leinsosint/Escritorio/dashboard-looker
source venv/bin/activate
python app.py
```

El servidor estará disponible en: **http://localhost:5000**

## Acceso al Dashboard

1. Abrir **Safari** en **iOS** (iPhone/iPad) o **macOS**
2. Navegar a: `http://localhost:5000` (o la IP del servidor)
3. Ingresar credenciales:
   - Usuario: `admin`
   - Contraseña: `admin123`
4. El dashboard de Looker Studio se cargará automáticamente

## Archivos Importantes

| Archivo | Descripción |
|---------|-------------|
| `app.py` | Aplicación Flask principal |
| `users.json` | Base de datos de usuarios (contraseñas hasheadas) |
| `templates/login.html` | Página de login con estilo naval |
| `templates/dashboard.html` | Dashboard con iframe de Looker Studio |
| `templates/blocked.html` | Página de navegador no soportado |
| `static/css/styles.css` | Estilos navales institucionales |

## Gestión de Usuarios

### Listar usuarios
```bash
python create_user.py list
```

### Crear nuevo usuario
```bash
python create_user.py create <usuario> <contraseña>
```

## Seguridad Implementada

- ✅ Contraseñas hasheadas con bcrypt
- ✅ Archivo `users.json` con permisos 600 (solo propietario)
- ✅ Restricción a Safari iOS/macOS solamente
- ✅ Sesiones de 8 horas de duración
- ✅ Middleware de detección de User Agent

## Características

- 🔐 Autenticación segura con Flask Sessions
- 🍎 Solo accesible desde Safari en iOS/macOS
- 🎨 Diseño naval institucional DINTEMAR
- 📊 Dashboard de Looker Studio embebido
- ⚡ Sesiones persistentes (8 horas)

## Solución de Problemas

### Error "No existe el archivo users.json"
Ya está creado. Si lo borras, ejecuta:
```bash
python create_user.py create admin admin123
```

### El iframe no carga
- Verificar conexión a internet
- Verificar que el URL de Looker Studio sea correcto
- Deshabilitar bloqueadores de publicidad en Safari

### Acceso denegado
Solo funciona en Safari iOS/macOS. Otros navegadores son bloqueados automáticamente.

## Información Técnica

- **Framework:** Flask 3.0.0
- **Hashing:** bcrypt 4.1.2
- **Python:** 3.8+
- **Puerto:** 5000 (configurable en app.py)

## Documentación Completa

Ver `README.md` para documentación detallada.

---

**DINTEMAR - Marina de Guerra del Perú**
© 2025 - Todos los derechos reservados

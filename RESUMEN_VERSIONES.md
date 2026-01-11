# Dashboard Looker Studio - Resumen de Versiones

## ✅ Creación Completada

Se han creado **tres versiones** del proyecto Dashboard Looker Studio para DINTEMAR.

---

## 📂 Estructura de Directorios

```
/home/leinsosint/Escritorio/
├── dashboard-looker/           # VERSIÓN 1: Básico (Red Local)
│   ├── app.py                  # Flask app
│   ├── create_user.py          # Gestión de usuarios
│   ├── users.json              # Base de datos (con usuario admin)
│   ├── install.sh              # Script instalación
│   ├── README.md               # Documentación
│   ├── templates/              # HTML navales
│   ├── static/css/             # Estilos navales
│   └── venv/                   # Entorno virtual ✅ ACTIVO
│
├── dashboard-looker-tailscale/ # VERSIÓN 2: Tailscale VPN ⭐
│   ├── app_tailscale.py        # Flask app (escucha en 0.0.0.0)
│   ├── create_user.py          # Gestión de usuarios
│   ├── install.sh              # Script instalación auto
│   ├── README_TAILSCALE.md     # Guía completa
│   ├── dashboard-tailscale.service  # Servicio systemd
│   ├── templates/              # HTML navales
│   └── static/css/             # Estilos navales
│
├── dashboard-looker-prod/      # VERSIÓN 3: Producción (nginx + HTTPS) 🚀
│   ├── app_prod.py             # Flask app (ProxyFix)
│   ├── create_user.py          # Gestión de usuarios
│   ├── install.sh              # Script instalación auto
│   ├── README_PROD.md          # Guía completa
│   ├── dashboard-nginx.conf    # Configuración nginx
│   ├── dashboard-prod.service  # Servicio systemd
│   ├── templates/              # HTML navales
│   └── static/css/             # Estilos navales
│
└── COMPARACION_VERSIONES.md    # Guía comparativa
```

---

## 🎯 Tres Versiones Disponibles

### 1️⃣ VERSIÓN BÁSICA (Red Local)
**Ubicación:** `/home/leinsosint/Escritorio/dashboard-looker/`

- ✅ **Instalada y funcionando** - Puerto 5000 activo
- ✅ **Usuario admin creado** - Contraseña: `admin123`
- ✅ **Entorno virtual activo** - venv configurado
- ✅ **Servidor corriendo** - PID 62000

**Acceso:** `http://192.168.18.229:5000` (solo red local)

**Para reiniciar:**
```bash
cd /home/leinsosint/Escritorio/dashboard-looker
source venv/bin/activate
python app.py
```

---

### 2️⃣ VERSIÓN TAILSCALE ⭐ (Recomendada)
**Ubicación:** `/home/leinsosint/Escritorio/dashboard-looker-tailscale/`

- 🔐 **VPN segura** - Acceso desde cualquier lugar
- 🌍 **Global** - Funciona en todo el mundo con VPN
- 💰 **Gratis** - Sin costos adicionales
- 🚀 **Fácil** - 15 minutos de instalación

**Instalación:**
```bash
cd /home/leinsosint/Escritorio/dashboard-looker-tailscale
sudo ./install.sh
```

**Documentación:** `README_TAILSCALE.md`

---

### 3️⃣ VERSIÓN PRODUCCIÓN 🚀 (nginx + HTTPS)
**Ubicación:** `/home/leinsosint/Escritorio/dashboard-looker-prod/`

- 🌐 **Pública** - Acceso desde internet
- 🔒 **HTTPS completo** - Let's Encrypt
- ⚡ **Performance** - nginx + Gunicorn
- 🛡️ **Hardening** - Rate limiting, security headers

**Instalación:**
```bash
cd /home/leinsosint/Escritorio/dashboard-looker-prod
sudo ./install.sh
```

**Documentación:** `README_PROD.md`

---

## 📊 Comparativa Rápida

| Característica | Básico | Tailscale | Producción |
|----------------|--------|-----------|------------|
| **Estado** | ✅ Activo | 🔧 Por instalar | 🔧 Por instalar |
| **Acceso** | Red local | Global (VPN) | Internet |
| **Seguridad** | Básica | Alta | Muy Alta |
| **Dominio** | No | No | Sí |
| **Costo** | $0 | $0 | ~$10/año |
| **Instalación** | 5 min | 15 min | 45 min |
| **Mantenimiento** | Muy bajo | Bajo | Medio |

---

## 🚀 ¿Cuál Usar?

### Para acceso en tu casa/oficina:
→ **Versión Básica** (ya está funcionando)

```bash
# Ya está activo, solo accede desde Safari:
http://192.168.18.229:5000
```

### Para acceso desde cualquier lugar:
→ **Versión Tailscale** ⭐ (recomendado)

```bash
cd /home/leinsosint/Escritorio/dashboard-looker-tailscale
sudo ./install.sh
```

### Para acceso público general:
→ **Versión Producción**

```bash
cd /home/leinsosint/Escritorio/dashboard-looker-prod
sudo ./install.sh
```

---

## 📱 Credenciales (Versión Básica)

- **URL:** `http://192.168.18.229:5000`
- **Usuario:** `admin`
- **Contraseña:** `admin123`

⚠️ **Importante:** Cambia la contraseña en producción

---

## 📖 Documentación Disponible

1. **COMPARACION_VERSIONES.md** - Comparación detallada
2. **dashboard-looker/README.md** - Versión básica
3. **dashboard-looker-tailscale/README_TAILSCALE.md** - Versión Tailscale
4. **dashboard-looker-prod/README_PROD.md** - Versión Producción

---

## 🛠️ Próximos Pasos

### Opción A: Mantener versión básica

Ya está funcionando. Solo ábrela desde Safari en red local.

### Opción B: Instalar Tailscale

```bash
cd /home/leinsosint/Escritorio/dashboard-looker-tailscale
sudo ./install.sh
```

Luego instala Tailscale en tu dispositivo iOS/macOS desde:
- iOS: App Store
- macOS: https://tailscale.com/download/mac

### Opción C: Instalar versión completa

```bash
cd /home/leinsosint/Escritorio/dashboard-looker-prod
sudo ./install.sh
```

Necesitarás un dominio propio (ej: dashboard.dintemar.mil.pe).

---

## 📞 Ayuda

Cada versión tiene su README con instrucciones detalladas de:
- Instalación
- Configuración
- Troubleshooting
- Seguridad

---

**DINTEMAR - Marina de Guerra del Perú**
© 2025 - Todos los derechos reservados

---

## ✨ Características Comunes a Todas las Versiones

- 🍎 **Solo Safari iOS/macOS** - Restricción de navegador
- 🎨 **Diseño naval institucional** - Estética DINTEMAR
- 🔐 **Autenticación segura** - bcrypt + Flask Sessions
- 📊 **Dashboard Looker embebido** - Iframe integrado
- ⚡ **Sesiones persistentes** - 8 horas de duración
- 🛡️ **Protección XSS** - Jinja2 sanitización

---

**¿Lista para elegir tu versión?**

Elige:
1. **Básico** - Ya está funcionando en red local
2. **Tailscale** - Instala con `sudo ./install.sh` en carpeta tailscale
3. **Producción** - Instala con `sudo ./install.sh` en carpeta prod

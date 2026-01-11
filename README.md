# 🧪 Muñeco de Pruebas - Dashboard

**Entorno de desarrollo y pruebas del Dashboard Flask**

---

## 📍 Ubicación

```
/home/leinsosint/Escritorio/muñeco de pruebas del dashboard
```

## 🎯 Propósito

Aquí puedes hacer **TODAS las modificaciones** y pruebas sin riesgo de romper nada en producción.

---

## 🚀 Flujo de Trabajo Rápido

### 1. Modificar archivos aquí
```bash
cd "/home/leinsosint/Escritorio/muñeco de pruebas del dashboard"
nano templates/dashboard.html
```

### 2. Probar localmente
```bash
source venv/bin/activate
python app_prod.py
# Abrir http://localhost:5001
```

### 3. Subir a GitHub
```bash
git add .
git commit -m "describe tus cambios"
git push origin master
```

### 4. Actualizar servidor (producción)
```bash
ssh root@64.225.50.194
cd /root/dashboard-looker-prod
cp app_prod.py app_prod.py.backup
git pull https://github.com/LeInS-dev/dashboard-looker-test.git
systemctl restart dashboard-prod
```

---

## 📖 Documentación Completa

Ver **`GUIA_MODIFICACIONES.md`** para instrucciones detalladas.

---

## ⚠️ REGLAS IMPORTANTES

1. ✅ **Modificar AQUÍ** (muñeco de pruebas)
2. ✅ **Probar AQUÍ** (localhost:5001)
3. ✅ **Subir AQUÍ** (git push)
4. ⚠️ **Solo después** → Actualizar producción

---

## 🌐 URLs

- **Muñeco de pruebas (local):** http://localhost:5001
- **Repositorio Git:** https://github.com/LeInS-dev/dashboard-looker-test
- **Producción:** https://minerv.duckdns.org

---

## 📂 Archivos Principales

| Archivo | Descripción |
|---------|-------------|
| `app_prod.py` | Aplicación Flask (SIN login) |
| `templates/dashboard.html` | Página principal |
| `templates/dossiers.html` | Sección dossiers |
| `static/css/styles.css` | Estilos CSS |
| `requirements.txt` | Dependencias Python |

---

## 🧪 Testing Checklist

Antes de subir a producción, verifica:

- [ ] Código modificado en muñeco de pruebas
- [ ] Probado localmente (`python app_prod.py`)
- [ ] Todas las rutas funcionan (`/` y `/dossiers`)
- [ ] Sin errores en consola del navegador
- [ ] Diseño se ve bien en Safari/Firefox
- [ ] Commit con mensaje descriptivo
- [ ] Push a GitHub exitoso

---

**¡Experimenta libremente aquí! 🎨**

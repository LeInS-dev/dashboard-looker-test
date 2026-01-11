# 🧪 GUÍA DE TRABAJO - MUÑECO DE PRUEBAS

**Propósito:** Este directorio es tu entorno de pruebas para hacer modificaciones al dashboard antes de subirlas a producción.

**Repositorio Git:** https://github.com/LeInS-dev/dashboard-looker-test

---

## 📋 FLUJO DE TRABAJO COMPLETO

### 1️⃣ HACER CAMBIOS EN EL MUÑECO DE PRUEBAS

```bash
# Entrar al directorio de pruebas
cd "/home/leinsosint/Escritorio/muñeco de pruebas del dashboard"

# Editar archivos
# - app_prod.py (lógica Flask)
# - templates/*.html (HTML)
# - static/css/*.css (estilos)

# Ejemplo con nano
nano templates/dashboard.html
```

### 2️⃣ PROBAR LOCALMENTE

```bash
# Activar entorno virtual
cd "/home/leinsosint/Escritorio/muñeco de pruebas del dashboard"
source venv/bin/activate

# Iniciar servidor de desarrollo
python app_prod.py

# El servidor correrá en http://127.0.0.1:5001
# Abre en tu navegador: http://localhost:5001
```

**IMPORTANTE:**
- Prueba TODAS las rutas: `/`, `/dossiers`
- Verifica que no haya errores en la consola
- Prueba en Safari/Firefox
- Verifica el diseño responsive (devtools del navegador)

### 3️⃣ CUANDO ESTÉ TODO BIEN, SUBIR A GITHUB

```bash
# Asegurarte de estar en el directorio de pruebas
cd "/home/leinsosint/Escritorio/muñeco de pruebas del dashboard"

# Verificar cambios
git status

# Agregar archivos modificados
git add .

# Hacer commit con mensaje claro
git commit -m "describe tus cambios aquí"

# Ejemplo:
# git commit -m "feat: Add new dossier section
# - Added templates/dossiers.html
# - Updated navbar with navigation
# - Added gradient backgrounds"

# Subir a GitHub
git push origin master
```

### 4️⃣ ACTUALIZAR PRODUCCIÓN (SERVIDOR)

```bash
# Conectar al servidor
ssh root@64.225.50.194

# Ir al directorio de producción
cd /root/dashboard-looker-prod

# Hacer backup rápido (POR SEGURIDAD)
cp app_prod.py app_prod.py.backup-$(date +%Y%m%d-%H%M)

# Actualizar desde GitHub
git pull origin master

# Si hay conflictos, resolverlos:
git stash
git pull origin master
git stash pop

# Reiniciar servicio
systemctl restart dashboard-prod

# Verificar que funcione
systemctl status dashboard-prod

# Salir del servidor
exit
```

### 5️⃣ VERIFICAR EN PRODUCCIÓN

```bash
# Abrir en navegador
# https://minerv.duckdns.org

# Verificar:
# - Carga la página
# - No hay errores 404/500
# - El diseño se ve bien
# - Las rutas funcionan
```

---

## 🚨 SI ALGO SALE MAL - ROLLBACK

```bash
# Conectar al servidor
ssh root@64.225.50.194

# Ir a producción
cd /root/dashboard-looker-prod

# Verificar archivos de backup
ls -la app_prod.py.backup-*

# Restaurar el backup más reciente
cp app_prod.py.backup-YYYYMMDD-HHMM app_prod.py

# Reiniciar servicio
systemctl restart dashboard-prod
```

---

## 📁 ESTRUCTURA DE ARCHIVOS IMPORTANTES

```
muñeco de pruebas del dashboard/
├── app_prod.py          # Lógica principal Flask (SIN login)
├── app.py               # Versión con login (NO USAR)
├── requirements.txt     # Dependencias Python
├── templates/
│   ├── dashboard.html   # Página principal
│   ├── dossiers.html    # Sección de dossiers
│   ├── 404.html         # Página no encontrada
│   ├── 500.html         # Error del servidor
│   └── blocked.html     # Navegador no permitido
└── static/
    └── css/
        └── styles.css    # Estilos
```

---

## ⚠️ REGLAS DE ORO

1. **NUNCA modificar directamente en producción**
   - Siempre modificar en el muñeco de pruebas
   - Probar localmente primero
   - Subir con git solo cuando funcione

2. **SIEMPRE hacer backup antes de git pull en producción**
   ```bash
   cp app_prod.py app_prod.py.backup
   ```

3. **Commits descriptivos**
   - ❌ `git commit -m "cambios"`
   - ✅ `git commit -m "fix: Resolve 404 error on dossiers page"`

4. **Probar TODO antes de subir**
   - Todas las rutas
   - Múltiples navegadores
   - Mobile y desktop

---

## 🔧 COMANDOS ÚTILES

### Ver qué cambió
```bash
git diff              # Cambios sin commit
git diff HEAD~1       # Cambios en el último commit
git log --oneline -5  # Últimos 5 commits
```

### Ver rutas de Flask
```bash
# En app_prod.py buscar:
@app.route('/')
```

### Logs de producción
```bash
ssh root@64.225.50.194 "journalctl -u dashboard-prod -n 50"
```

### Ver memoria RAM
```bash
ssh root@64.225.50.194 "ps aux | grep app_prod"
```

---

## 📊 CHECKLIST ANTES DE SUBIR A PRODUCCIÓN

- [ ] Código modificado en muñeco de pruebas
- [ ] Probado localmente (`python app_prod.py`)
- [ ] Todas las rutas funcionan (/ y /dossiers)
- [ ] Sin errores en consola del navegador
- [ ] Diseño se ve bien en Safari/Firefox
- [ ] Commit con mensaje descriptivo
- [ ] Push a GitHub exitoso
- [ ] Backup hecho en servidor antes de pull

---

## 🎯 EJEMPLO REAL

Supongamos que quieres cambiar el color del navbar:

```bash
# PASO 1: Modificar
cd "/home/leinsosint/Escritorio/muñeco de pruebas del dashboard"
nano static/css/styles.css
# Cambiar color de .navbar

# PASO 2: Probar local
source venv/bin/activate
python app_prod.py
# Abrir http://localhost:5001 y verificar

# PASO 3: Subir cambios
git add static/css/styles.css
git commit -m "style: Update navbar color to purple"
git push origin master

# PASO 4: Actualizar producción
ssh root@64.225.50.194
cd /root/dashboard-looker-prod
cp app_prod.py app_prod.py.backup
git pull origin master
systemctl restart dashboard-prod
exit

# PASO 5: Verificar
# Abrir https://minerv.duckdns.org en navegador
```

---

**Recuerda:** El muñeco de pruebas es tu zona segura. Aquí puedes equivocarte sin romper nada en producción. ¡Experimenta libremente!

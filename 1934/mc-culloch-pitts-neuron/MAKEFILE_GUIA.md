# 🛠️ Guía de Uso del Makefile

Este Makefile simplifica la gestión del entorno virtual Python con comandos fáciles de recordar.

## 📋 Comandos Disponibles

### 🔧 Gestión del Entorno Virtual

#### `make` o `make help`
Muestra todos los comandos disponibles con descripciones.

```bash
make
```

#### `make venv`
Crea el entorno virtual si no existe.

```bash
make venv
```

#### `make activate`
Muestra instrucciones para activar el entorno virtual manualmente.

```bash
make activate
```

**Salida:**
```
Para ACTIVAR el entorno virtual manualmente:
  source venv/bin/activate

Para DESACTIVAR:
  deactivate
```

#### `make shell` ⭐ **RECOMENDADO**
Abre una nueva shell con el entorno virtual **automáticamente activado**.

```bash
make shell
```

Esta es la forma más cómoda de trabajar. No necesitas activar/desactivar manualmente.
Cuando termines, simplemente escribe `exit` para salir y el entorno se desactiva automáticamente.

---

### 📦 Gestión de Dependencias

#### `make install`
Instala todas las dependencias desde `requirements.txt`.

```bash
make install
```

#### `make install-dev`
Instala dependencias comunes para desarrollo (numpy, matplotlib, pytest, etc.).

```bash
make install-dev
```

Incluye:
- numpy
- matplotlib
- pytest
- black
- flake8
- ipython
- jupyter

#### `make freeze`
Guarda todas las dependencias actuales en `requirements.txt`.

```bash
make freeze
```

#### `make update`
Actualiza todas las dependencias a sus últimas versiones.

```bash
make update
```

#### `make add PKG=nombre_paquete`
Instala un paquete específico.

```bash
make add PKG=numpy
make add PKG="numpy==1.24.0"  # Versión específica
```

#### `make remove PKG=nombre_paquete`
Desinstala un paquete específico.

```bash
make remove PKG=numpy
```

---

### 📊 Información y Estado

#### `make info`
Muestra información detallada del entorno virtual.

```bash
make info
```

**Salida:**
```
📍 Ubicación: /path/to/proyecto/venv
🐍 Python: Python 3.13.7
📦 pip: versión 25.2
🔧 Ejecutable: /path/to/proyecto/venv/bin/python
```

#### `make status`
Muestra el estado y lista todos los paquetes instalados.

```bash
make status
```

#### `make size`
Muestra el tamaño del entorno virtual.

```bash
make size
```

---

### 🚀 Ejecución

#### `make run`
Ejecuta el programa principal (`main.py` o `mcculloch_pitts.py`).

```bash
make run
```

#### `make test`
Ejecuta las pruebas (pytest).

```bash
make test
```

#### `make jupyter`
Abre Jupyter Notebook (si está instalado).

```bash
make jupyter
```

---

### 🧹 Limpieza

#### `make clean`
Elimina archivos temporales (`__pycache__`, `*.pyc`, etc.).

```bash
make clean
```

#### `make clean-venv`
Elimina completamente el entorno virtual (pide confirmación).

```bash
make clean-venv
```

#### `make reset`
Elimina y recrea el entorno virtual desde cero.

```bash
make reset
```

---

### 🔍 Diagnóstico

#### `make check`
Verifica que Python y las herramientas necesarias estén instaladas en el sistema.

```bash
make check
```

---

## 🎯 Flujos de Trabajo Comunes

### 1️⃣ **Comenzar un Nuevo Proyecto**

```bash
# Crear el entorno
make venv

# Instalar herramientas de desarrollo
make install-dev

# Guardar las dependencias
make freeze

# Abrir shell para trabajar
make shell
```

### 2️⃣ **Trabajar en un Proyecto Existente**

```bash
# Crear entorno e instalar dependencias
make venv
make install

# Abrir shell
make shell

# Trabajar normalmente...
# Cuando termines, salir
exit
```

### 3️⃣ **Agregar una Nueva Dependencia**

```bash
# Instalar el paquete
make add PKG=numpy

# Actualizar requirements.txt
make freeze

# Verificar instalación
make status
```

### 4️⃣ **Usar el Entorno para Trabajo Diario** ⭐

```bash
# Opción 1: Usar make shell (recomendado)
make shell
# Ahora estás en el entorno, trabaja normalmente
python mi_script.py
pip install nuevo_paquete
exit  # Sale y desactiva

# Opción 2: Activación manual tradicional
source venv/bin/activate
python mi_script.py
deactivate
```

### 5️⃣ **Limpiar y Reiniciar**

```bash
# Limpiar archivos temporales
make clean

# Recrear entorno desde cero
make reset

# O manualmente:
make clean-venv
make venv
make install
```

### 6️⃣ **Compartir el Proyecto**

```bash
# Asegúrate de tener requirements.txt actualizado
make freeze

# Añadir a git
git add requirements.txt Makefile

# Otra persona puede recrear el entorno con:
make venv
make install
```

---

## 💡 Consejos y Trucos

### Alias Útiles

Agrega estos alias a tu `~/.bashrc` o `~/.zshrc`:

```bash
# Alias para comandos make comunes
alias mshell='make shell'
alias minstall='make install'
alias mfreeze='make freeze'
alias mstatus='make status'
alias mclean='make clean'
```

Luego solo necesitas escribir:
```bash
mshell    # en lugar de make shell
minstall  # en lugar de make install
```

### Verificar Estado Rápidamente

```bash
# Ver qué hay instalado
make status | less

# Buscar un paquete específico
make status | grep numpy
```

### Instalar Múltiples Paquetes

```bash
# Método 1: Uno por uno
make add PKG=numpy
make add PKG=matplotlib
make add PKG=pandas

# Método 2: Editar requirements.txt y luego
make install

# No olvides guardar
make freeze
```

### Debugging

```bash
# Verificar que todo está OK
make check

# Ver información del entorno
make info

# Ver paquetes instalados
make status
```

---

## 🔥 Características Especiales

### 🎨 Colores en la Salida
El Makefile usa colores para hacer la salida más legible:
- 🟢 **Verde**: Éxito y confirmaciones
- 🟡 **Amarillo**: Advertencias y sugerencias
- 🔵 **Azul**: Información

### 🛡️ Confirmación de Seguridad
Comandos destructivos como `make clean-venv` piden confirmación antes de ejecutarse.

### 📝 Mensajes Informativos
Cada comando proporciona feedback claro sobre qué está haciendo y sugerencias sobre qué hacer después.

### ⚡ Shell Interactiva Mejorada
`make shell` te abre una shell completamente configurada:
- ✅ Entorno virtual activado
- ✅ Prompt personalizado que muestra `(venv)`
- ✅ Mensajes de bienvenida con información del entorno
- ✅ Al salir con `exit`, todo se limpia automáticamente

---

## 🐛 Solución de Problemas

### Error: "make: command not found"

**Solución:** Instala make:
```bash
# Ubuntu/Debian
sudo apt-get install build-essential

# Manjaro/Arch
sudo pacman -S base-devel

# macOS
xcode-select --install
```

### Error: "python: command not found"

**Solución:** Instala Python 3:
```bash
# Ubuntu/Debian
sudo apt-get install python3 python3-venv

# Manjaro/Arch
sudo pacman -S python

# macOS
brew install python
```

### El entorno no se activa correctamente

**Solución:** Usa `make shell` en lugar de intentar activar manualmente.

### Los paquetes no se instalan

```bash
# Verificar que el entorno existe
make info

# Recrear desde cero
make reset

# Verificar dependencias del sistema
make check
```

---

## 📚 Comparación: Con y Sin Makefile

### ❌ Sin Makefile (tradicional)

```bash
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip list
pip freeze > requirements.txt
deactivate
```

### ✅ Con Makefile

```bash
make venv
make shell
make status
make freeze
exit
```

**Mucho más simple y fácil de recordar.**

---

## 🎓 Comandos en Orden de Uso Frecuente

1. `make shell` - El más usado, para trabajar en el proyecto
2. `make install` - Al clonar o actualizar proyecto
3. `make status` - Ver qué hay instalado
4. `make freeze` - Guardar dependencias
5. `make add PKG=...` - Agregar paquetes
6. `make clean` - Limpiar archivos temporales
7. `make info` - Ver información del entorno
8. `make run` - Ejecutar el programa
9. `make reset` - Cuando algo sale mal

---

## 🌟 Resumen Ejecutivo

El Makefile convierte comandos complejos en simples palabras:

| Tarea | Comando Tradicional | Con Makefile |
|-------|-------------------|--------------|
| Crear entorno | `python -m venv venv` | `make venv` |
| Activar | `source venv/bin/activate` | `make shell` |
| Instalar deps | `pip install -r requirements.txt` | `make install` |
| Guardar deps | `pip freeze > requirements.txt` | `make freeze` |
| Ver paquetes | `pip list` | `make status` |
| Limpiar | `find . -name "__pycache__"...` | `make clean` |

**¡Trabaja más rápido y con menos errores!** 🚀


# 🐍 Guía Completa de Entornos Virtuales en Python

## 📚 ¿Qué es un Entorno Virtual?

Un **entorno virtual** es un directorio autocontenido que incluye:
- Una instalación de Python
- Bibliotecas y paquetes específicos
- Scripts para activación/desactivación

## 🎯 ¿Para qué sirven?

### Aislamiento de Dependencias
Cada proyecto tiene sus propias dependencias sin conflictos con otros proyectos.

**Ejemplo del problema:**
```
Sistema Global:
├── Python 3.13
└── numpy==1.20.0

Proyecto A necesita: numpy==1.20.0 ✅
Proyecto B necesita: numpy==1.24.0 ❌ CONFLICTO!
```

**Solución con entornos virtuales:**
```
Sistema Global:
└── Python 3.13

Proyecto A:
└── venv/ → numpy==1.20.0 ✅

Proyecto B:
└── venv/ → numpy==1.24.0 ✅
```

### Ventajas principales:

1. **Reproducibilidad**: Cualquiera puede recrear el entorno exacto
2. **Limpieza**: No contaminas tu instalación global de Python
3. **Seguridad**: Puedes experimentar sin miedo a romper otros proyectos
4. **Portabilidad**: Fácil de compartir con otros desarrolladores

## 🔧 Estructura de un Entorno Virtual

Tu entorno virtual `venv/` contiene:

```
venv/
├── bin/                    # Scripts ejecutables (Linux/Mac)
│   ├── activate            # Script de activación para bash/zsh
│   ├── activate.csh        # Para csh/tcsh
│   ├── activate.fish       # Para fish shell
│   ├── Activate.ps1        # Para PowerShell
│   ├── pip                 # Gestor de paquetes
│   ├── pip3                # Alias de pip
│   ├── python              # Enlace al intérprete Python
│   └── python3             # Alias de python
├── include/                # Archivos de cabecera C
├── lib/                    # Bibliotecas Python instaladas
│   └── python3.13/
│       └── site-packages/  # Aquí se instalan los paquetes
├── lib64 -> lib            # Enlace simbólico
└── pyvenv.cfg              # Configuración del entorno
```

### 📄 Archivo `pyvenv.cfg`

Este archivo contiene la configuración:

```
home = /usr/bin
include-system-site-packages = false
version = 3.13.7
executable = /usr/bin/python3.13
```

- `home`: Ubicación del Python del sistema
- `include-system-site-packages`: Si puede acceder a paquetes globales (false = aislado)
- `version`: Versión de Python
- `executable`: Ruta al ejecutable de Python base

## 🚀 Cómo Manipular Entornos Virtuales

### 1. Crear un entorno virtual

```bash
# Método estándar (Python 3.3+)
python -m venv nombre_entorno

# Usando virtualenv (más antiguo pero con más opciones)
pip install virtualenv
virtualenv nombre_entorno
```

### 2. Activar el entorno virtual

**Linux/Mac:**
```bash
source venv/bin/activate
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

**¿Qué hace la activación?**

1. Modifica la variable `PATH` para que `python` apunte al del entorno virtual
2. Cambia el prompt para mostrar `(venv)`
3. Establece la variable `VIRTUAL_ENV`

Verificar:
```bash
which python    # Debe mostrar: .../venv/bin/python
echo $VIRTUAL_ENV  # Muestra la ruta del entorno
```

### 3. Instalar paquetes

```bash
# Activar primero el entorno
source venv/bin/activate

# Instalar un paquete
pip install numpy

# Instalar versión específica
pip install numpy==1.24.3

# Instalar múltiples paquetes
pip install numpy matplotlib pandas

# Instalar desde requirements.txt
pip install -r requirements.txt
```

### 4. Gestionar dependencias

```bash
# Ver paquetes instalados
pip list

# Ver paquetes con árbol de dependencias
pip show numpy

# Guardar todas las dependencias
pip freeze > requirements.txt

# Actualizar un paquete
pip install --upgrade numpy

# Desinstalar un paquete
pip uninstall numpy
```

### 5. Desactivar el entorno

```bash
deactivate
```

Esto restaura tu configuración de Python al sistema global.

## 🛠️ Comandos Útiles

### Verificar qué Python estás usando

```bash
# Antes de activar
which python     # /usr/bin/python
python --version # Python 3.13.7

# Después de activar
which python     # /path/to/venv/bin/python
python --version # Python 3.13.7 (mismo, pero aislado)
```

### Clonar un entorno

No se recomienda copiar directorios `venv/`. En su lugar:

```bash
# En el proyecto original
pip freeze > requirements.txt

# En el nuevo proyecto
python -m venv nuevo_venv
source nuevo_venv/bin/activate
pip install -r requirements.txt
```

### Eliminar un entorno

```bash
# Desactivar primero
deactivate

# Simplemente eliminar el directorio
rm -rf venv/
```

### Recrear desde cero

```bash
rm -rf venv/
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🔍 Cómo Funciona Internamente

### 1. Cuando activas el entorno:

El script `activate` hace esto:

```bash
# Guarda el PATH original
_OLD_VIRTUAL_PATH="$PATH"

# Añade el bin del venv al inicio del PATH
export PATH="/path/to/venv/bin:$PATH"

# Establece la variable VIRTUAL_ENV
export VIRTUAL_ENV="/path/to/venv"

# Modifica el prompt
export PS1="(venv) $PS1"
```

### 2. Cuando ejecutas `pip install`:

1. `pip` se ejecuta desde `venv/bin/pip`
2. Instala paquetes en `venv/lib/python3.13/site-packages/`
3. NO afecta la instalación global de Python

### 3. Cuando ejecutas `python`:

1. El sistema busca en `PATH` (modificado por `activate`)
2. Encuentra primero `venv/bin/python`
3. Python busca módulos en `venv/lib/python3.13/site-packages/`

## 📋 Mejores Prácticas

### ✅ Hacer:

1. **Un entorno por proyecto**
   ```
   proyecto1/
   └── venv/
   
   proyecto2/
   └── venv/
   ```

2. **Agregar venv/ al .gitignore**
   ```gitignore
   venv/
   .venv/
   env/
   ```

3. **Mantener requirements.txt actualizado**
   ```bash
   pip freeze > requirements.txt
   ```

4. **Usar nombres consistentes**
   - `venv/` (recomendado)
   - `.venv/` (oculto)
   - `env/`

5. **Documentar versión de Python**
   ```bash
   python --version > .python-version
   ```

### ❌ Evitar:

1. ❌ Commitear el directorio `venv/` a Git
2. ❌ Mover o copiar directorios `venv/` entre sistemas
3. ❌ Instalar paquetes globalmente cuando trabajas en un proyecto
4. ❌ Compartir el mismo entorno entre múltiples proyectos

## 🎓 Ejemplo Práctico Completo

```bash
# 1. Crear proyecto
mkdir mi_proyecto
cd mi_proyecto

# 2. Crear entorno virtual
python -m venv venv

# 3. Activar
source venv/bin/activate

# 4. Instalar dependencias
pip install numpy matplotlib pandas

# 5. Guardar dependencias
pip freeze > requirements.txt

# 6. Trabajar en tu código
echo "import numpy as np" > main.py
echo "print(np.array([1, 2, 3]))" >> main.py

# 7. Ejecutar
python main.py

# 8. Cuando termines
deactivate

# --- En otro momento o máquina ---

# 9. Recrear entorno
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🆚 Alternativas a venv

### virtualenv
- Más antiguo, más opciones
- Compatible con Python 2
```bash
pip install virtualenv
virtualenv venv
```

### conda
- Para ciencia de datos
- Gestiona dependencias no-Python también
```bash
conda create -n myenv python=3.13
conda activate myenv
```

### poetry
- Gestor moderno de dependencias
- Maneja entornos automáticamente
```bash
poetry init
poetry add numpy
```

### pipenv
- Combina pip y virtualenv
- Usa Pipfile en lugar de requirements.txt
```bash
pipenv install numpy
pipenv shell
```

## 🐛 Solución de Problemas

### Problema: "command not found: activate"

```bash
# Usar source
source venv/bin/activate
```

### Problema: PowerShell no permite ejecutar scripts

```powershell
# Cambiar política de ejecución (una vez)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Problema: pip instala en global en lugar de venv

```bash
# Verificar que el entorno está activado
echo $VIRTUAL_ENV

# Verificar qué pip estás usando
which pip
# Debe mostrar: /path/to/venv/bin/pip
```

### Problema: Módulo no encontrado después de instalar

```bash
# Asegúrate de estar usando el Python del venv
which python

# Reinstalar el paquete
pip uninstall nombre_paquete
pip install nombre_paquete
```

## 📚 Recursos Adicionales

- [Documentación oficial de venv](https://docs.python.org/3/library/venv.html)
- [PEP 405 - Python Virtual Environments](https://www.python.org/dev/peps/pep-0405/)
- [Real Python - Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/)

---

**Recuerda:** Los entornos virtuales son tu mejor amigo en Python. Úsalos siempre, incluso para proyectos pequeños. Tu yo del futuro te lo agradecerá. 🙏


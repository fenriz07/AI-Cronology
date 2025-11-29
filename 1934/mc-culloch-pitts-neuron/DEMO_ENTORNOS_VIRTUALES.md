# 🧪 Demostración Práctica de Entornos Virtuales

## Experimento: Ver el aislamiento en acción

### 1️⃣ Estado ANTES de activar el entorno virtual

```bash
$ which python
/usr/bin/python

$ python --version
Python 3.13.7

$ echo $VIRTUAL_ENV
(vacío - sin entorno virtual activo)
```

**Python del sistema global**: `/usr/bin/python`

---

### 2️⃣ Estado DESPUÉS de activar el entorno virtual

```bash
$ source venv/bin/activate

(venv) $ which python
/home/servio/Documentos/ai-cronology/1934/mc-culloch-pitts-neuron/venv/bin/python

(venv) $ python --version
Python 3.13.7

(venv) $ echo $VIRTUAL_ENV
/home/servio/Documentos/ai-cronology/1934/mc-culloch-pitts-neuron/venv
```

**Python del entorno virtual**: `venv/bin/python`

---

### 🔍 ¿Qué cambió?

| Aspecto | Sin activar | Con venv activado |
|---------|-------------|-------------------|
| **Ubicación de python** | `/usr/bin/python` | `/path/to/proyecto/venv/bin/python` |
| **Variable VIRTUAL_ENV** | (vacía) | `/path/to/proyecto/venv` |
| **Prompt del shell** | `$` | `(venv) $` |
| **PATH** | Sistema normal | `venv/bin` al inicio |
| **Paquetes disponibles** | Globales del sistema | Solo los de venv/ |

---

### 📦 Paquetes instalados inicialmente

```
Package  Version
-------  -------
pip      25.2
```

Solo viene con `pip` instalado. **Entorno completamente limpio**.

---

## 🎯 Ejercicio práctico: Instalar y usar numpy

### Paso 1: Instalar numpy (solo en el entorno virtual)

```bash
(venv) $ pip install numpy
Collecting numpy
  Downloading numpy-2.x.x-cp313-cp313-manylinux_2_17_x86_64.whl
Installing collected packages: numpy
Successfully installed numpy-2.x.x
```

### Paso 2: Verificar instalación

```bash
(venv) $ pip list
Package Version
------- -------
numpy   2.x.x
pip     25.2

(venv) $ python -c "import numpy; print(numpy.__version__)"
2.x.x
```

### Paso 3: Desactivar y verificar aislamiento

```bash
(venv) $ deactivate

$ which python
/usr/bin/python

$ python -c "import numpy; print(numpy.__version__)"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'numpy'
```

**¡Numpy NO está en el sistema global!** Solo existe en el entorno virtual.

---

## 🔧 Comandos de manipulación práctica

### Ver información del entorno

```bash
# Ubicación del Python que estás usando
(venv) $ which python

# Dónde se instalan los paquetes
(venv) $ python -c "import site; print(site.getsitepackages())"

# Variable de entorno activa
(venv) $ echo $VIRTUAL_ENV
```

### Gestionar paquetes

```bash
# Listar paquetes instalados
(venv) $ pip list

# Buscar un paquete específico
(venv) $ pip show numpy

# Ver árbol de dependencias
(venv) $ pip show numpy | grep Requires

# Actualizar un paquete
(venv) $ pip install --upgrade numpy

# Instalar versión específica
(venv) $ pip install numpy==1.24.0

# Desinstalar
(venv) $ pip uninstall numpy
```

### Guardar y compartir el entorno

```bash
# Guardar todas las dependencias
(venv) $ pip freeze > requirements.txt

# Ver el contenido
(venv) $ cat requirements.txt
numpy==2.x.x

# Otra persona puede recrear el entorno
$ python -m venv nuevo_venv
$ source nuevo_venv/bin/activate
(nuevo_venv) $ pip install -r requirements.txt
```

---

## 💡 Caso de uso real: Proyecto McCulloch-Pitts

```bash
# 1. Activar entorno
$ source venv/bin/activate

# 2. Instalar dependencias para el proyecto
(venv) $ pip install numpy matplotlib

# 3. Crear el código
(venv) $ cat > mcculloch_pitts.py << 'EOF'
import numpy as np

def mcculloch_pitts_neuron(inputs, weights, threshold):
    """
    Implementación de la neurona de McCulloch-Pitts (1943).
    
    Args:
        inputs: Array de entradas binarias (0 o 1)
        weights: Array de pesos (pueden ser negativos)
        threshold: Umbral de activación
    
    Returns:
        1 si la suma ponderada >= umbral, 0 en caso contrario
    """
    weighted_sum = np.dot(inputs, weights)
    return 1 if weighted_sum >= threshold else 0

# Ejemplo: Puerta AND
inputs = np.array([1, 1])
weights = np.array([1, 1])
threshold = 2

output = mcculloch_pitts_neuron(inputs, weights, threshold)
print(f"Entradas: {inputs}")
print(f"Salida (AND): {output}")
EOF

# 4. Ejecutar
(venv) $ python mcculloch_pitts.py

# 5. Guardar dependencias
(venv) $ pip freeze > requirements.txt

# 6. Verificar
(venv) $ cat requirements.txt
```

---

## 🎭 Comparación visual del aislamiento

```
┌─────────────────────────────────────────┐
│      Sistema Operativo (Linux)          │
│  ┌─────────────────────────────────┐   │
│  │  Python Global (/usr/bin/python)│   │
│  │  • pip 25.2                      │   │
│  │  • (sin otros paquetes)          │   │
│  └─────────────────────────────────┘   │
│                                          │
│  ┌─────────────────────────────────┐   │
│  │  Proyecto 1                      │   │
│  │  └─ venv/                        │   │
│  │     • Python 3.13 (enlace)       │   │
│  │     • numpy==1.20.0              │   │
│  │     • matplotlib==3.5.0          │   │
│  └─────────────────────────────────┘   │
│                                          │
│  ┌─────────────────────────────────┐   │
│  │  Proyecto 2 (mc-culloch-pitts)   │   │
│  │  └─ venv/                        │   │
│  │     • Python 3.13 (enlace)       │   │
│  │     • numpy==2.1.0 (diferente!)  │   │
│  │     • matplotlib==3.9.0          │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

Cada proyecto tiene sus propias versiones sin conflictos.

---

## 🐛 Debugging: ¿Dónde está mi paquete?

```bash
# ¿Estoy en el entorno virtual?
$ echo $VIRTUAL_ENV
# Si está vacío, NO estás en un venv

# Activar correctamente
$ source venv/bin/activate

# ¿Qué Python estoy usando?
(venv) $ which python
# Debe ser: /path/to/tu/proyecto/venv/bin/python

# ¿Dónde busca Python los módulos?
(venv) $ python -c "import sys; print('\n'.join(sys.path))"

# ¿Está instalado el paquete?
(venv) $ pip show nombre_paquete

# ¿En qué versión?
(venv) $ pip list | grep nombre_paquete
```

---

## ✨ Resumen ejecutivo

**Un entorno virtual es como una "caja de arena" para tu proyecto Python:**

- ✅ Cada proyecto tiene su propia caja
- ✅ Lo que instalas en una caja no afecta a las otras
- ✅ Puedes destruir y recrear cajas sin problemas
- ✅ Puedes compartir la "receta" (requirements.txt) con otros

**Regla de oro:** Siempre activa el entorno virtual antes de trabajar en un proyecto.

```bash
# Inicio de cada sesión de trabajo
cd mi_proyecto
source venv/bin/activate
# ¡Ahora puedes trabajar!
```


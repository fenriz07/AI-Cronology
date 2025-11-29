# Makefile para gestión del entorno virtual Python
# Proyecto: McCulloch-Pitts Neuron (1934)

# Variables
VENV_NAME := venv
PYTHON := python
VENV_BIN := $(VENV_NAME)/bin
VENV_PYTHON := $(VENV_BIN)/python
VENV_PIP := $(VENV_BIN)/pip
REQ_FILE := requirements.txt

# Colores para mensajes
GREEN := \033[0;32m
YELLOW := \033[0;33m
BLUE := \033[0;34m
RED := \033[0;31m
RESET := \033[0m

# Target por defecto
.DEFAULT_GOAL := help

# Phony targets (no son archivos reales)
.PHONY: help venv activate install install-dev freeze update clean test run info status

# Ayuda: muestra todos los comandos disponibles
help:
	@printf "$(BLUE)╔════════════════════════════════════════════════════╗$(RESET)\n"
	@printf "$(BLUE)║  Makefile - McCulloch-Pitts Neuron Environment    ║$(RESET)\n"
	@printf "$(BLUE)╚════════════════════════════════════════════════════╝$(RESET)\n\n"
	@printf "$(GREEN)Comandos de Entorno Virtual:$(RESET)\n"
	@printf "  $(YELLOW)make venv$(RESET)          - Crea el entorno virtual\n"
	@printf "  $(YELLOW)make activate$(RESET)      - Muestra cómo activar el entorno\n"
	@printf "  $(YELLOW)make shell$(RESET)         - Abre una shell con el entorno activado\n\n"
	@printf "$(GREEN)Gestión de Dependencias:$(RESET)\n"
	@printf "  $(YELLOW)make install$(RESET)       - Instala dependencias desde requirements.txt\n"
	@printf "  $(YELLOW)make install-dev$(RESET)   - Instala dependencias de desarrollo\n"
	@printf "  $(YELLOW)make freeze$(RESET)        - Guarda dependencias actuales\n"
	@printf "  $(YELLOW)make update$(RESET)        - Actualiza todas las dependencias\n\n"
	@printf "$(GREEN)Utilidades:$(RESET)\n"
	@printf "  $(YELLOW)make info$(RESET)          - Información del entorno virtual\n"
	@printf "  $(YELLOW)make status$(RESET)        - Estado del entorno y paquetes instalados\n"
	@printf "  $(YELLOW)make test$(RESET)          - Ejecuta pruebas (si existen)\n"
	@printf "  $(YELLOW)make run$(RESET)           - Ejecuta el programa principal\n"
	@printf "  $(YELLOW)make clean$(RESET)         - Limpia archivos temporales\n"
	@printf "  $(YELLOW)make clean-venv$(RESET)    - Elimina el entorno virtual\n"
	@printf "  $(YELLOW)make reset$(RESET)         - Recrea el entorno desde cero\n\n"
	@printf "$(GREEN)Ejemplo de uso:$(RESET)\n"
	@printf "  1. make venv              # Crear entorno\n"
	@printf "  2. make install           # Instalar dependencias\n"
	@printf "  3. make shell             # Trabajar en el entorno\n"
	@printf "  4. exit                   # Salir del entorno\n\n"

# Crea el entorno virtual
venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate:
	@printf "$(GREEN)📦 Creando entorno virtual...$(RESET)\n"
	$(PYTHON) -m venv $(VENV_NAME)
	@printf "$(GREEN)✅ Entorno virtual creado en: $(VENV_NAME)/$(RESET)\n"
	@printf "$(YELLOW)💡 Usa 'make activate' para ver cómo activarlo$(RESET)\n"

# Muestra instrucciones para activar manualmente
activate:
	@printf "$(BLUE)╔════════════════════════════════════════════════════╗$(RESET)\n"
	@printf "$(BLUE)║  Para ACTIVAR el entorno virtual manualmente:     ║$(RESET)\n"
	@printf "$(BLUE)╚════════════════════════════════════════════════════╝$(RESET)\n\n"
	@printf "$(GREEN)En Linux/Mac:$(RESET)\n"
	@printf "  source $(VENV_NAME)/bin/activate\n\n"
	@printf "$(GREEN)En Windows (CMD):$(RESET)\n"
	@printf "  $(VENV_NAME)\\Scripts\\activate.bat\n\n"
	@printf "$(GREEN)En Windows (PowerShell):$(RESET)\n"
	@printf "  $(VENV_NAME)\\Scripts\\Activate.ps1\n\n"
	@printf "$(YELLOW)💡 Mejor opción: usa 'make shell' para abrir una shell con el entorno activado$(RESET)\n\n"
	@printf "$(BLUE)Para DESACTIVAR:$(RESET)\n"
	@printf "  deactivate\n\n"

# Abre una nueva shell con el entorno virtual activado
shell: venv
	@printf "$(GREEN)🐚 Abriendo shell con entorno virtual activado...$(RESET)\n"
	@printf "$(YELLOW)💡 Escribe 'exit' para salir y desactivar el entorno$(RESET)\n\n"
	@bash --init-file <(echo ". $(HOME)/.bashrc 2>/dev/null || true; source $(VENV_BIN)/activate; \
		printf '$(GREEN)✅ Entorno virtual activado$(RESET)\n'; \
		printf '$(YELLOW)📍 Ubicación: $(shell pwd)/$(VENV_NAME)$(RESET)\n'; \
		printf '$(BLUE)🐍 Python: $$($(VENV_PYTHON) --version)$(RESET)\n\n'; \
		PS1='(venv) \[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$$ '")

# Instala las dependencias desde requirements.txt
install: venv
	@if [ -f "$(REQ_FILE)" ]; then \
		printf "$(GREEN)📥 Instalando dependencias desde $(REQ_FILE)...$(RESET)\n"; \
		$(VENV_PIP) install --upgrade pip; \
		$(VENV_PIP) install -r $(REQ_FILE); \
		printf "$(GREEN)✅ Dependencias instaladas$(RESET)\n"; \
	else \
		printf "$(YELLOW)⚠️  No existe $(REQ_FILE)$(RESET)\n"; \
		printf "$(BLUE)💡 Crea el archivo o usa 'make install-dev' para instalar paquetes básicos$(RESET)\n"; \
	fi

# Instala dependencias de desarrollo
install-dev: venv
	@printf "$(GREEN)📥 Instalando dependencias de desarrollo...$(RESET)\n"
	$(VENV_PIP) install --upgrade pip
	$(VENV_PIP) install numpy matplotlib pytest black flake8 ipython jupyter
	@printf "$(GREEN)✅ Dependencias de desarrollo instaladas$(RESET)\n"
	@printf "$(YELLOW)💡 Usa 'make freeze' para guardar las dependencias$(RESET)\n"

# Guarda las dependencias actuales en requirements.txt
freeze: venv
	@printf "$(GREEN)💾 Guardando dependencias en $(REQ_FILE)...$(RESET)\n"
	$(VENV_PIP) freeze > $(REQ_FILE)
	@printf "$(GREEN)✅ Dependencias guardadas$(RESET)\n\n"
	@printf "$(BLUE)Contenido de $(REQ_FILE):$(RESET)\n"
	@cat $(REQ_FILE)

# Actualiza todas las dependencias
update: venv
	@printf "$(GREEN)🔄 Actualizando pip...$(RESET)\n"
	$(VENV_PIP) install --upgrade pip
	@if [ -f "$(REQ_FILE)" ]; then \
		printf "$(GREEN)🔄 Actualizando dependencias...$(RESET)\n"; \
		$(VENV_PIP) install --upgrade -r $(REQ_FILE); \
		printf "$(GREEN)✅ Dependencias actualizadas$(RESET)\n"; \
		printf "$(YELLOW)💡 Usa 'make freeze' para guardar las nuevas versiones$(RESET)\n"; \
	else \
		printf "$(YELLOW)⚠️  No existe $(REQ_FILE)$(RESET)\n"; \
	fi

# Muestra información del entorno virtual
info: venv
	@printf "$(BLUE)╔════════════════════════════════════════════════════╗$(RESET)\n"
	@printf "$(BLUE)║  Información del Entorno Virtual                  ║$(RESET)\n"
	@printf "$(BLUE)╚════════════════════════════════════════════════════╝$(RESET)\n\n"
	@printf "$(GREEN)📍 Ubicación:$(RESET) $(shell pwd)/$(VENV_NAME)\n"
	@printf "$(GREEN)🐍 Python:$(RESET) $(shell $(VENV_PYTHON) --version)\n"
	@printf "$(GREEN)📦 pip:$(RESET) versión $(shell $(VENV_PIP) --version | cut -d' ' -f2)\n"
	@printf "$(GREEN)🔧 Ejecutable:$(RESET) $(shell readlink -f $(VENV_PYTHON))\n\n"
	@printf "$(BLUE)Variables de entorno:$(RESET)\n"
	@$(VENV_PYTHON) -c "import sys; print('  VIRTUAL_ENV:', '$(shell pwd)/$(VENV_NAME)')"
	@$(VENV_PYTHON) -c "import sys; print('  sys.prefix:', sys.prefix)"
	@printf "\n"

# Muestra el estado y paquetes instalados
status: venv
	@printf "$(BLUE)╔════════════════════════════════════════════════════╗$(RESET)\n"
	@printf "$(BLUE)║  Estado del Entorno Virtual                       ║$(RESET)\n"
	@printf "$(BLUE)╚════════════════════════════════════════════════════╝$(RESET)\n\n"
	@if [ -d "$(VENV_NAME)" ]; then \
		printf "$(GREEN)✅ Entorno virtual: CREADO$(RESET)\n\n"; \
	else \
		printf "$(YELLOW)❌ Entorno virtual: NO CREADO$(RESET)\n\n"; \
	fi
	@printf "$(BLUE)📦 Paquetes instalados:$(RESET)\n"
	@$(VENV_PIP) list
	@printf "\n$(BLUE)📊 Total de paquetes:$(RESET) $(shell $(VENV_PIP) list | tail -n +3 | wc -l)\n"

# Ejecuta pruebas (si existen)
test: venv
	@if [ -d "tests" ] || [ -f "test_*.py" ]; then \
		printf "$(GREEN)🧪 Ejecutando pruebas...$(RESET)\n"; \
		$(VENV_PYTHON) -m pytest -v; \
	else \
		printf "$(YELLOW)⚠️  No se encontraron pruebas$(RESET)\n"; \
		printf "$(BLUE)💡 Crea archivos test_*.py o un directorio tests/$(RESET)\n"; \
	fi

# Ejecuta el programa principal
run: venv
	@if [ -f "main.py" ]; then \
		printf "$(GREEN)🚀 Ejecutando main.py...$(RESET)\n"; \
		$(VENV_PYTHON) main.py; \
	elif [ -f "mcculloch_pitts.py" ]; then \
		printf "$(GREEN)🚀 Ejecutando mcculloch_pitts.py...$(RESET)\n"; \
		$(VENV_PYTHON) mcculloch_pitts.py; \
	else \
		printf "$(YELLOW)⚠️  No se encontró archivo principal$(RESET)\n"; \
		printf "$(BLUE)💡 Crea main.py o especifica el archivo:$(RESET)\n"; \
		printf "    $(VENV_PYTHON) tu_archivo.py\n"; \
	fi

# Limpia archivos temporales
clean:
	@printf "$(GREEN)🧹 Limpiando archivos temporales...$(RESET)\n"
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@find . -type f -name "*.pyo" -delete 2>/dev/null || true
	@find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".coverage" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	@printf "$(GREEN)✅ Limpieza completada$(RESET)\n"

# Elimina el entorno virtual
clean-venv:
	@printf "$(YELLOW)⚠️  ¿Estás seguro de eliminar el entorno virtual?$(RESET)\n"
	@printf "$(YELLOW)   Presiona Ctrl+C para cancelar o Enter para continuar...$(RESET)\n"
	@read confirm
	@printf "$(GREEN)🗑️  Eliminando entorno virtual...$(RESET)\n"
	@rm -rf $(VENV_NAME)
	@printf "$(GREEN)✅ Entorno virtual eliminado$(RESET)\n"

# Recrea el entorno virtual desde cero
reset: clean-venv venv install
	@printf "$(GREEN)✅ Entorno recreado exitosamente$(RESET)\n"

# Verificación de dependencias del sistema
check:
	@printf "$(BLUE)🔍 Verificando dependencias del sistema...$(RESET)\n\n"
	@command -v python >/dev/null 2>&1 && \
		printf "$(GREEN)✅ Python: $(shell python --version)$(RESET)\n" || \
		printf "$(RED)❌ Python no encontrado$(RESET)\n"
	@command -v pip >/dev/null 2>&1 && \
		printf "$(GREEN)✅ pip: instalado$(RESET)\n" || \
		printf "$(RED)❌ pip no encontrado$(RESET)\n"
	@python -m venv --help >/dev/null 2>&1 && \
		printf "$(GREEN)✅ venv: disponible$(RESET)\n" || \
		printf "$(RED)❌ venv no disponible$(RESET)\n"
	@printf "\n"

# Instala un paquete específico (uso: make add PKG=numpy)
add: venv
	@if [ -z "$(PKG)" ]; then \
		printf "$(YELLOW)⚠️  Debes especificar un paquete$(RESET)\n"; \
		printf "$(BLUE)Uso: make add PKG=nombre_paquete$(RESET)\n"; \
		printf "$(BLUE)Ejemplo: make add PKG=numpy$(RESET)\n"; \
	else \
		printf "$(GREEN)📥 Instalando $(PKG)...$(RESET)\n"; \
		$(VENV_PIP) install $(PKG); \
		printf "$(GREEN)✅ $(PKG) instalado$(RESET)\n"; \
		printf "$(YELLOW)💡 Usa 'make freeze' para guardar en requirements.txt$(RESET)\n"; \
	fi

# Desinstala un paquete específico (uso: make remove PKG=numpy)
remove: venv
	@if [ -z "$(PKG)" ]; then \
		printf "$(YELLOW)⚠️  Debes especificar un paquete$(RESET)\n"; \
		printf "$(BLUE)Uso: make remove PKG=nombre_paquete$(RESET)\n"; \
		printf "$(BLUE)Ejemplo: make remove PKG=numpy$(RESET)\n"; \
	else \
		printf "$(GREEN)🗑️  Desinstalando $(PKG)...$(RESET)\n"; \
		$(VENV_PIP) uninstall -y $(PKG); \
		printf "$(GREEN)✅ $(PKG) desinstalado$(RESET)\n"; \
		printf "$(YELLOW)💡 Usa 'make freeze' para actualizar requirements.txt$(RESET)\n"; \
	fi

# Abre Jupyter Notebook (si está instalado)
jupyter: venv
	@if $(VENV_PIP) show jupyter >/dev/null 2>&1; then \
		printf "$(GREEN)📓 Iniciando Jupyter Notebook...$(RESET)\n"; \
		$(VENV_BIN)/jupyter notebook; \
	else \
		printf "$(YELLOW)⚠️  Jupyter no está instalado$(RESET)\n"; \
		printf "$(BLUE)💡 Instálalo con: make add PKG=jupyter$(RESET)\n"; \
	fi

# Muestra el tamaño del entorno virtual
size:
	@if [ -d "$(VENV_NAME)" ]; then \
		printf "$(BLUE)📊 Tamaño del entorno virtual:$(RESET)\n"; \
		du -sh $(VENV_NAME); \
	else \
		printf "$(YELLOW)⚠️  El entorno virtual no existe$(RESET)\n"; \
	fi

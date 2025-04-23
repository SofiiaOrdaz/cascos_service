# 👷 Cascos Service

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Ultralytics YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-blueviolet)](https://ultralytics.com/)

Servicio para la detección de cascos en imágenes utilizando un modelo YOLOv8 preentrenado.

## 📚 Tabla de Contenidos

- [👷 Cascos Service](#-cascos-service)
  - [📚 Tabla de Contenidos](#-tabla-de-contenidos)
  - [🎯 Descripción del Proyecto](#-descripción-del-proyecto)
  - [📂 Estructura del Repositorio](#-estructura-del-repositorio)
  - [🚀 Instalación](#-instalación)
  - [▶️ Uso](#️-uso)
  - [🧪 Pruebas](#-pruebas)

## 🎯 Descripción del Proyecto

Este proyecto implementa un sistema para detectar cascos de seguridad en imágenes estáticas. Utiliza un modelo [YOLOv8](https://ultralytics.com/) preentrenado (`hemletYoloV8_100epochs.pt`) alojado en la carpeta `data/models`.

La lógica principal del servicio reside en el paquete `src/cascos_service`.

## 📂 Estructura del Repositorio

```txt
cascos_service/
│
├── .gitignore            # ⚙️ Archivos ignorados por Git
├── data/                 # 📊 Datos (modelos, imágenes, etc.)
│   ├── images/
│   │   └── casco4.jpg
│   └── models/
│       └── hemletYoloV8_100epochs.pt
├── notebooks/            # 📓 Notebooks para experimentación
│   └── CASCOS.ipynb
├── src/                  # 🐍 Código fuente del paquete
│   └── cascos_service/   # 📦 Paquete Python principal
│       ├── __init__.py
│       ├── core/         # ✨ Lógica central (detección)
│       │   ├── __init__.py
│       │   └── detection.py
│       ├── config/       # ⚙️ Configuración (rutas)
│       │   ├── __init__.py
│       │   └── settings.py
│       ├── utils/        # 🛠️ Utilidades (visualización)
│       │   ├── __init__.py
│       │   └── visualization.py
│       └── cli.py        # ▶️ Punto de entrada (línea de comandos)
├── tests/                # ✔️ Pruebas (pytest)
│   ├── __init__.py
│   └── test_detection.py
├── requirements.txt      # 📦 Dependencias Python
└── README.md             # 📄 Esta documentación
```

- **`data/`**: Almacena datos como imágenes y modelos.
- **`notebooks/`**: Contiene cuadernos Jupyter para análisis y demostraciones.
- **`src/cascos_service/`**: El corazón del proyecto, organizado como un paquete Python instalable.
  - `core/`: Módulos con la lógica principal (ej: `detection.py`).
  - `config/`: Gestión de la configuración (ej: `settings.py` con rutas).
  - `utils/`: Funciones de utilidad (ej: `visualization.py`).
  - `cli.py`: Script para interactuar con el servicio desde la línea de comandos.
- **`tests/`**: Pruebas automatizadas (usando `pytest`).
- **`requirements.txt`**: Lista de librerías Python necesarias.
- **`.gitignore`**: Especifica qué archivos no deben incluirse en Git.

## 🚀 Instalación

1. **Clonar el repositorio:**

    ```bash
    git clone https://github.com/SofiiaOrdaz/cascos_service.git
    cd cascos_service
    ```

2. **Crear entorno virtual e instalar dependencias:**
    Se recomienda usar un entorno virtual.

    ```bash
    # Crear entorno virtual
    python -m venv venv
    # Activar entorno
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate

    # Instalar librerías desde requirements.txt
    pip install -r requirements.txt
    ```

    *Nota: Si planeas ejecutar las pruebas, instala también `pytest`: `pip install pytest`*

## ▶️ Uso

El servicio se ejecuta a través del script `src/cascos_service/cli.py`. Puedes ejecutarlo directamente:

```bash
python src/cascos_service/cli.py [OPCIONES]
```

**Opciones disponibles:**

- `--image RUTA`: Especifica la ruta a la imagen a procesar (por defecto usa `data/images/casco4.jpg`).
- `--model RUTA`: Especifica la ruta al modelo `.pt` (por defecto usa `data/models/hemletYoloV8_100epochs.pt`).
- `--conf UMBRAL`: Define el umbral de confianza para las detecciones (por defecto `0.25`).
- `--device {auto,cpu,mps,cuda}`: Selecciona el dispositivo de cómputo (por defecto `auto`).
- `--mode {full,demo}`: Controla la salida.
  - `full`: Muestra la imagen anotada y los detalles de detección en consola (por defecto).
  - `demo`: Solo muestra la imagen anotada.
- `--no-save`: Evita que se guarden los resultados (imagen anotada) en la carpeta `runs/`.

**Ejemplo (usando valores por defecto):**

```bash
python src/cascos_service/cli.py
```

**Ejemplo (especificando imagen y usando modo demo):**

```bash
python src/cascos_service/cli.py --image ruta/a/otra/imagen.jpg --mode demo
```

## 🧪 Pruebas

Para ejecutar las pruebas automatizadas (ubicadas en la carpeta `tests/`), necesitas tener `pytest` instalado (`pip install pytest`).

Desde la raíz del proyecto, ejecuta:

```bash
pytest
```

Esto descubrirá y ejecutará automáticamente las pruebas definidas en `tests/test_detection.py`, verificando la carga del modelo y la funcionalidad básica de detección.

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

Este proyecto implementa un sistema para detectar cascos de seguridad en imágenes estáticas. Utiliza un modelo [YOLOv8](https://ultralytics.com/) preentrenado (`hemletYoloV8_100epochs.pt`).

Aunque el `README` inicial menciona herramientas para procesar video e integrar Kafka, la implementación actual se centra principalmente en el análisis de imágenes individuales.

## 📂 Estructura del Repositorio

```bash
cascos_service/
├── data/
│   ├── images/       # 🖼️ Imágenes de prueba (ej: casco4.jpg)
│   ├── models/       # 🧠 Modelos preentrenados (ej: hemletYoloV8_100epochs.pt)
│   └── video/        # 🎥 (Potencialmente para videos)
├── notebooks/
│   └── CASCOS.ipynb  # 📓 Notebook explicativo paso a paso
├── libs/             # 🧩 (Potencialmente para módulos auxiliares como Kafka)
├── scripts/          # 📜 (Potencialmente para scripts de video/demo)
├── main.py           # ▶️ Script principal para detección en imágenes
├── main_apple.py     # 🍏 Script optimizado para Apple MPS
├── main_demo.py      # ✨ Script de demostración simplificado
├── test.py           # ✔️ Script para pruebas básicas (carga de modelo)
└── README.md         # 📄 Esta documentación
```

- **`data/`**: Almacena los datos necesarios.
  - `images/`: Contiene las imágenes a procesar.
  - `models/`: Guarda los archivos del modelo YOLOv8 entrenado.
- **`notebooks/`**: Cuadernos Jupyter para exploración y explicación.
  - `CASCOS.ipynb`: Demuestra el proceso de detección.
- **`main.py`**: Ejecuta la detección en una imagen, muestra el resultado y la información detallada.
- **`main_apple.py`**: Variante de `main.py` que intenta usar la GPU de Apple (MPS).
- **`main_demo.py`**: Versión simplificada para una demostración visual rápida.
- **`test.py`**: Script básico para verificar la carga del modelo.

## 🚀 Instalación

1. **Clonar el repositorio:**

    ```bash
    git clone https://github.com/SofiiaOrdaz/cascos_service.git
    cd cascos_service
    ```

2. **Instalar dependencias:**
    Se recomienda usar un entorno virtual.

    ```bash
    # Crear entorno virtual (opcional pero recomendado)
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate

    # Instalar librerías
    pip install ultralytics matplotlib opencv-python torch
    ```

    *Nota: `opencv-python` es necesario para algunas funcionalidades de `ultralytics` y `matplotlib` para mostrar imágenes.*
    *Nota: `torch` es necesario si se usa `main_apple.py` o para asegurar compatibilidad con `ultralytics`.*

## ▶️ Uso

Puedes ejecutar los diferentes scripts principales según tus necesidades:

- **Ejecución estándar (muestra imagen y detalles):**

    ```bash
    python main.py
    ```

- **Ejecución optimizada para Apple MPS (si aplica):**

    ```bash
    python main_apple.py
    ```

- **Demostración rápida (solo muestra imagen):**

    ```bash
    python main_demo.py
    ```

Los scripts buscarán el modelo en `data/models/` y la imagen en `data/images/`. Las imágenes resultantes con las detecciones se guardarán automáticamente en una carpeta `runs/detect/`.

## 🧪 Pruebas

Para verificar que el modelo se carga correctamente:

```bash
python test.py
```

Deberías ver un mensaje "Carga del modelo: OK".

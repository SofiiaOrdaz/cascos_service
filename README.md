# Cascos Service

Este repositorio implementa un servicio para la detección de cascos utilizando modelos preentrenados (por ejemplo, YOLOv8). Además, incluye herramientas para procesar video e integrar la comunicación mediante Kafka.

## Estructura del Repositorio

- **libs/**:  
  Contiene módulos auxiliares, como `queues.py`, que facilita la integración con Kafka y otras utilidades.

- **data/**:  
  Carpeta destinada a almacenar datos de entrada:
  - `models/`: Modelos preentrenados (ej.: `hemletYoloV8_100epochs.pt`).
  - `images/`: Imágenes de prueba (ej.: `casco4.jpg`).
  - `video/`: Videos de prueba.
  - `bbox.txt`: Archivo con las coordenadas de la región de interés.

- **notebooks/**:  
  Notebooks de demostración (por ejemplo, un notebook que muestre la detección de cascos paso a paso).

- **scripts/**:  
  Scripts para la ejecución de demos, como `demo.py` para procesar video.

- **main.py**:  
  Script principal que integra la detección y permite ejecutar el servicio.

- **main_apple.py**:  
  Versión adaptada para dispositivos Apple (por ejemplo, utilizando MPS).

- **test.py**:  
  Scripts para pruebas unitarias y validación de módulos.

- **README.md**:  
  Este archivo, con información sobre el proyecto.

## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/SofiiaOrdaz/cascos_service.git
   cd cascos_service

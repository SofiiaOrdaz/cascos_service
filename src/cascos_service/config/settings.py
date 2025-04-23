import os

# Define el directorio base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Rutas relativas a la carpeta 'data'
DATA_DIR = os.path.join(BASE_DIR, "data")
IMAGES_DIR = os.path.join(DATA_DIR, "images")
MODELS_DIR = os.path.join(DATA_DIR, "models")

# Rutas específicas a archivos (ejemplos)
DEFAULT_IMAGE_PATH = os.path.join(IMAGES_DIR, "casco4.jpg")
DEFAULT_MODEL_PATH = os.path.join(MODELS_DIR, "hemletYoloV8_100epochs.pt") 
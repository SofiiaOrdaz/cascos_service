import torch
from ultralytics import YOLO
from ..config import settings  # Importar configuración relativa

def get_device(requested_device: str = "auto") -> torch.device:
    """Selecciona el dispositivo computacional (CPU, MPS, CUDA)."""
    if requested_device.lower() == "mps" and torch.backends.mps.is_available():
        print("Usando dispositivo MPS (Apple Silicon)")
        return torch.device("mps")
    elif requested_device.lower() == "cuda" and torch.cuda.is_available():
        print("Usando dispositivo CUDA (NVIDIA GPU)")
        return torch.device("cuda")
    else:
        if requested_device.lower() not in ["auto", "cpu"]:
             print(f"Dispositivo '{requested_device}' no disponible o no soportado, usando CPU.")
        print("Usando dispositivo CPU")
        return torch.device("cpu")

def detect_helmets(
    image_path: str = settings.DEFAULT_IMAGE_PATH,
    model_path: str = settings.DEFAULT_MODEL_PATH,
    conf_threshold: float = 0.25,
    device_name: str = "auto",
    save_results: bool = True
):
    """
    Carga un modelo YOLOv8 y detecta cascos en una imagen.

    Args:
        image_path (str): Ruta a la imagen.
        model_path (str): Ruta al modelo .pt.
        conf_threshold (float): Umbral de confianza para la detección.
        device_name (str): Dispositivo a usar ('auto', 'cpu', 'mps', 'cuda').
        save_results (bool): Si guardar la imagen anotada y resultados.

    Returns:
        list: Lista de resultados de la predicción de Ultralytics.
    """
    try:
        model = YOLO(model_path)
        print(f"Modelo cargado desde: {model_path}")

        device = get_device(device_name)
        # Mover el modelo al dispositivo si no es CPU (YOLO maneja CPU automáticamente)
        if device.type != 'cpu':
             model.to(device)
             print(f"Modelo movido al dispositivo: {device.type}")

        print(f"Realizando predicción en imagen: {image_path}")
        results = model.predict(
            source=image_path,
            conf=conf_threshold,
            save=save_results,
            device=device # Especificar dispositivo aquí también es buena práctica
        )
        print("Predicción completada.")
        return results

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo del modelo en '{model_path}' o la imagen en '{image_path}'.")
        return None
    except Exception as e:
        print(f"Error durante la detección: {e}")
        return None 
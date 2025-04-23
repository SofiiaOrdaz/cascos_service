import pytest
import sys
import os

# Añadir src al sys.path para encontrar los módulos del proyecto
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(project_root, 'src'))

from cascos_service.core.detection import detect_helmets
from cascos_service.config import settings

@pytest.mark.skipif(not os.path.exists(settings.DEFAULT_MODEL_PATH), reason="Modelo de prueba no encontrado")
@pytest.mark.skipif(not os.path.exists(settings.DEFAULT_IMAGE_PATH), reason="Imagen de prueba no encontrada")
def test_helmet_detection_on_sample():
    """Prueba la detección en la imagen y modelo por defecto."""
    print(f"Test: Usando modelo {settings.DEFAULT_MODEL_PATH}")
    print(f"Test: Usando imagen {settings.DEFAULT_IMAGE_PATH}")
    results = detect_helmets(
        image_path=settings.DEFAULT_IMAGE_PATH,
        model_path=settings.DEFAULT_MODEL_PATH,
        conf_threshold=0.25,
        device_name='cpu', # Forzar CPU para consistencia en tests
        save_results=False # No guardar resultados durante el test
    )

    assert results is not None, "La función de detección devolvió None"
    assert len(results) > 0, "La lista de resultados está vacía"
    # Verificar si hay detecciones (boxes)
    assert results[0].boxes is not None, "El objeto 'boxes' no está presente en los resultados"
    # Podríamos añadir más aserciones, como verificar el número de detecciones si es conocido
    # num_detections = len(results[0].boxes)
    # assert num_detections > 0, "No se detectó ningún objeto (casco)"
    print("Test de detección básica completado con éxito.")

# Podríamos añadir un test para verificar la carga del modelo explícitamente
def test_model_loading_path():
     """Verifica que la ruta al modelo por defecto existe."""
     assert os.path.exists(settings.DEFAULT_MODEL_PATH), f"El archivo del modelo no existe en {settings.DEFAULT_MODEL_PATH}"
     print(f"Test de existencia de modelo en {settings.DEFAULT_MODEL_PATH}: OK")

# Para ejecutar estos tests, necesitarás instalar pytest: pip install pytest
# Y luego ejecutar `pytest` en la raíz del proyecto. 
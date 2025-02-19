import os
from ultralytics import YOLO

def test_model_loading():
    model_path = os.path.join("data", "models", "hemletYoloV8_100epochs.pt")
    try:
        model = YOLO(model_path)
        print("Carga del modelo: OK")
    except Exception as e:
        print("Error al cargar el modelo:", e)

if __name__ == "__main__":
    test_model_loading()

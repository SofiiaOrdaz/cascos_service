import matplotlib.pyplot as plt
from ultralytics import YOLO
import cv2
import os

def main():
    # Ruta al modelo preentrenado
    model_path = os.path.join("data", "models", "hemletYoloV8_100epochs.pt")
    
    # Cargar el modelo YOLOv8
    model = YOLO(model_path)
    print("Modelo cargado correctamente.")
    
    # Ruta de la imagen de prueba
    image_path = os.path.join("data", "images", "casco4.jpg")
    
    # Realizar predicción
    results = model.predict(source=image_path, conf=0.25, save=True)
    
    # Obtener la imagen anotada
    annotated_image = results[0].plot()
    
    # Mostrar la imagen anotada
    plt.figure(figsize=(10, 6))
    plt.imshow(annotated_image)
    plt.axis('off')
    plt.show()
    
    # Información adicional de las detecciones
    print("Coordenadas (xyxy):", results[0].boxes.xyxy.cpu().numpy())
    print("Confianza:", results[0].boxes.conf.cpu().numpy())
    print("Clases detectadas:", results[0].boxes.cls.cpu().numpy())
    print("Nombres de las clases detectadas:",
          [results[0].names[int(cls)] for cls in results[0].boxes.cls.cpu().numpy()])

if __name__ == "__main__":
    main()

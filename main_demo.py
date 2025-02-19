import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO
import os

def demo_image_detection():
    model_path = os.path.join("data", "models", "hemletYoloV8_100epochs.pt")
    image_path = os.path.join("data", "images", "casco4.jpg")
    
    model = YOLO(model_path)
    results = model.predict(source=image_path, conf=0.25, save=True)
    
    annotated_image = results[0].plot()
    
    plt.figure(figsize=(10, 6))
    plt.imshow(annotated_image)
    plt.axis('off')
    plt.title("Detección de Casco")
    plt.show()

def main():
    print("Ejecutando demo de detección de cascos...")
    demo_image_detection()

if __name__ == "__main__":
    main()

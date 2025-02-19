import torch
import matplotlib.pyplot as plt
from ultralytics import YOLO
import os

def get_device():
    if torch.backends.mps.is_available():
        print("Usando dispositivo MPS")
        return torch.device("mps")
    else:
        print("Usando dispositivo CPU")
        return torch.device("cpu")

def main():
    device = get_device()
    model_path = os.path.join("data", "models", "hemletYoloV8_100epochs.pt")
    image_path = os.path.join("data", "images", "casco4.jpg")
    
    model = YOLO(model_path)
    # Si es necesario, puedes mover el modelo al dispositivo
    model.model.to(device)
    
    results = model.predict(source=image_path, conf=0.25, save=True)
    annotated_image = results[0].plot()
    
    plt.figure(figsize=(10, 6))
    plt.imshow(annotated_image)
    plt.axis('off')
    plt.title("Detección de Casco en Apple/MPS")
    plt.show()

if __name__ == "__main__":
    main()

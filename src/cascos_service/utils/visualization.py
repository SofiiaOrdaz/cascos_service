import matplotlib.pyplot as plt
from ultralytics.engine.results import Results
import numpy as np

def display_results(results: list[Results], show_details: bool = True):
    """
    Muestra la imagen anotada y opcionalmente los detalles de la detección.

    Args:
        results (list[Results]): Lista de resultados de Ultralytics.
        show_details (bool): Si imprimir detalles numéricos en consola.
    """
    if not results or not results[0].boxes:
        print("No se encontraron detecciones para mostrar.")
        # Aún así, podríamos intentar mostrar la imagen original si existe
        try:
            original_img = results[0].orig_img
            plt.figure(figsize=(10, 6))
            # Matplotlib espera RGB, YOLOv8 usa BGR por defecto con OpenCV
            plt.imshow(cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB))
            plt.title("Imagen Original (Sin Detecciones)")
            plt.axis('off')
            plt.show()
        except Exception as e:
            print(f"No se pudo mostrar la imagen original: {e}")
        return

    # Obtener y mostrar la imagen anotada
    try:
        annotated_image = results[0].plot()  # Esto devuelve un ndarray BGR
        plt.figure(figsize=(10, 6))
        # Convertir BGR a RGB para Matplotlib
        plt.imshow(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        plt.title("Resultados de Detección de Cascos")
        plt.show()
    except Exception as e:
        print(f"Error al mostrar la imagen anotada: {e}")
        # Intentar importar cv2 aquí si falla la conversión BGR->RGB
        try:
            import cv2
            annotated_image = results[0].plot()
            plt.figure(figsize=(10, 6))
            plt.imshow(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB))
            plt.axis('off')
            plt.title("Resultados de Detección de Cascos (Intento 2)")
            plt.show()
        except ImportError:
            print("Error: OpenCV (cv2) no está instalado. No se puede convertir BGR a RGB para mostrar la imagen.")
        except Exception as e_inner:
             print(f"Error persistente al mostrar la imagen: {e_inner}")


    # Mostrar detalles si se solicita
    if show_details:
        print("\n--- Detalles de la Detección ---")
        try:
            boxes = results[0].boxes
            print(f"Coordenadas (xyxy):\n{boxes.xyxy.cpu().numpy()}")
            print(f"\nConfianza:\n{boxes.conf.cpu().numpy()}")
            print(f"\nClases detectadas (índices):\n{boxes.cls.cpu().numpy()}")

            # Obtener nombres de clases si están disponibles
            if results[0].names:
                detected_classes_names = [results[0].names[int(cls)] for cls in boxes.cls.cpu().numpy()]
                print(f"\nNombres de las clases detectadas:\n{detected_classes_names}")
            else:
                print("\nNombres de clases no disponibles en los resultados.")
        except Exception as e:
            print(f"Error al obtener detalles de las detecciones: {e}")

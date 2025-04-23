import argparse
import sys
import os

# Ajustar PYTHONPATH para encontrar módulos locales si se ejecuta como script
# Esto es útil durante el desarrollo antes de instalar el paquete
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from cascos_service.core.detection import detect_helmets
from cascos_service.utils.visualization import display_results
from cascos_service.config import settings

def main():
    parser = argparse.ArgumentParser(description="Detectar cascos en una imagen usando YOLOv8.")

    parser.add_argument(
        "--image",
        type=str,
        default=settings.DEFAULT_IMAGE_PATH,
        help=f"Ruta a la imagen de entrada (por defecto: {settings.DEFAULT_IMAGE_PATH})"
    )
    parser.add_argument(
        "--model",
        type=str,
        default=settings.DEFAULT_MODEL_PATH,
        help=f"Ruta al modelo .pt (por defecto: {settings.DEFAULT_MODEL_PATH})"
    )
    parser.add_argument(
        "--conf",
        type=float,
        default=0.25,
        help="Umbral de confianza para la detección (por defecto: 0.25)"
    )
    parser.add_argument(
        "--device",
        type=str,
        default="auto",
        choices=["auto", "cpu", "mps", "cuda"],
        help="Dispositivo a usar (auto, cpu, mps, cuda) (por defecto: auto)"
    )
    parser.add_argument(
        "--mode",
        type=str,
        default="full",
        choices=["full", "demo"],
        help="Modo de ejecución: 'full' (muestra imagen y detalles), 'demo' (solo imagen) (por defecto: full)"
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        help="Evita guardar la imagen anotada y los resultados en la carpeta 'runs'"
    )

    args = parser.parse_args()

    print("--- Iniciando Detección de Cascos ---")
    results = detect_helmets(
        image_path=args.image,
        model_path=args.model,
        conf_threshold=args.conf,
        device_name=args.device,
        save_results=not args.no_save
    )

    if results:
        print("--- Mostrando Resultados ---")
        display_results(
            results=results,
            show_details=(args.mode == "full")
        )
    else:
        print("No se generaron resultados para mostrar.")

    print("--- Proceso Finalizado ---")

if __name__ == "__main__":
    main() 
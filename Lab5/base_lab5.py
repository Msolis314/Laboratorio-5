import argparse
from PIL import Image
import cv2
import matplotlib.pyplot as plt

class ImageProcessor:
    def __init__(self, library):
        self.library = library

    def open_image(self, path):
        if self.library == 'PIL':
            return Image.open(path)
        elif self.library == 'OpenCV':
            return cv2.imread(path)
        else:
            raise ValueError("Biblioteca no válida")

    def show_image(self, image):
        if self.library == 'PIL':
            image.show()
        elif self.library == 'Matplotlib':
            plt.imshow(image)
            plt.show()
        elif self.library == 'OpenCV':
            cv2.imshow('Imagen', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            raise ValueError("Biblioteca no válida")

def parse_args():
    parser = argparse.ArgumentParser(description="Procesamiento de Imágenes")
    parser.add_argument("--biblioteca", choices=["PIL", "Matplotlib", "OpenCV"], required=True, help="Biblioteca para procesamiento de imágenes")
    parser.add_argument("--imagen", required=True, help="Ruta de la imagen a procesar")
    return parser.parse_args()

def main():
    args = parse_args()

    try:
        processor = ImageProcessor(args.biblioteca)
        image = processor.open_image(args.imagen)
        processor.show_image(image)
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")

if __name__ == "__main__":
    main()
